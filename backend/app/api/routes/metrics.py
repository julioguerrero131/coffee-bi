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
