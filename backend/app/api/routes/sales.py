from fastapi import APIRouter, HTTPException
from app.schemas.sale import Sale
from app.core.db import db

from app.core.config import settings

router = APIRouter()

@router.post("/")
def create_sale(sale: Sale):
    """
    Agrega un nuevo ticket de venta a la base de datos.
    """
    try:
        # Convert Pydantic model to dictionary
        sale_dict = sale.model_dump()
        
        # Inserción en la colección usando la variable de entorno
        result = db[settings.MONGO_COLLECTION_SALES].insert_one(sale_dict)
        
        return {
            "status": "success",
            "message": "Ticket agregado correctamente",
            "id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
