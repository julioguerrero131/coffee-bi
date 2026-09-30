from fastapi import APIRouter, Query, HTTPException
from app.core.db import db
from app.core.config import settings

router = APIRouter()

@router.get("/sales")
def get_sales(
    skip: int = Query(0, ge=0, description="Número de registros a omitir para la paginación"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
):
    """
    Obtiene las ventas ordenadas de la más reciente a la más antigua (por fecha_hora) con paginación.
    """
    try:
        # Buscamos en la colección, ordenamos por 'fecha_hora' descendente (-1), y aplicamos skip y limit
        cursor = db[settings.MONGO_COLLECTION_SALES].find().sort("fecha_hora", -1).skip(skip).limit(limit)
        
        sales = []
        for sale in cursor:
            # Mongo devuelve el _id como un objeto ObjectId, lo convertimos a string para el JSON
            sale["_id"] = str(sale["_id"])
            sales.append(sale)
            
        # Opcional: contar el total de documentos para saber cuántas páginas hay en total
        total_documents = db[settings.MONGO_COLLECTION_SALES].count_documents({})
            
        return {
            "status": "success",
            "pagination": {
                "total": total_documents,
                "skip": skip,
                "limit": limit
            },
            "data": sales
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sales-by-month")
def get_sales_by_month(
    year: int = Query(..., description="Filtrar ventas por un año específico")
):
    """
    Obtiene el total de ventas y la cantidad de tickets agrupados por mes para un año específico.
    """
    try:
        pipeline = [
            {
                "$addFields": {
                    "fecha_hora_date": { "$toDate": "$fecha_hora" }
                }
            },
            {
                "$match": {
                    "$expr": {"$eq": [{"$year": "$fecha_hora_date"}, year]}
                }
            },
            {
                "$group": {
                    "_id": {
                        "year": {"$year": "$fecha_hora_date"},
                        "month": {"$month": "$fecha_hora_date"}
                    },
                    "total_sales": {"$sum": "$monto"},
                    "ticket_count": {"$sum": 1}
                }
            },
            {
                "$sort": {"_id.year": 1, "_id.month": 1}
            }
        ]
        
        cursor = db[settings.MONGO_COLLECTION_SALES].aggregate(pipeline)
        
        data = []
        for result in cursor:
            data.append({
                "year": result["_id"]["year"],
                "month": result["_id"]["month"],
                "total_sales": result["total_sales"],
                "ticket_count": result["ticket_count"]
            })
            
        return {
            "status": "success",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sales-by-product")
def get_sales_by_product(
    year: int = Query(..., description="Filtrar ventas por producto para un año específico (ej. 2024)")
):
    """
    Obtiene el total de ventas y la cantidad de tickets agrupados por producto para un año específico.
    """
    try:
        pipeline = [
            {
                "$addFields": {
                    "fecha_hora_date": { "$toDate": "$fecha_hora" }
                }
            },
            {
                "$match": {
                    "$expr": {"$eq": [{"$year": "$fecha_hora_date"}, year]}
                }
            },
            {
                "$group": {
                    "_id": "$producto",
                    "total_sales": {"$sum": "$monto"},
                    "ticket_count": {"$sum": 1}
                }
            },
            {
                "$sort": {"total_sales": -1}
            }
        ]
        
        cursor = db[settings.MONGO_COLLECTION_SALES].aggregate(pipeline)
        
        data = []
        for result in cursor:
            data.append({
                "product": result["_id"],
                "total_sales": result["total_sales"],
                "ticket_count": result["ticket_count"]
            })
            
        return {
            "status": "success",
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
