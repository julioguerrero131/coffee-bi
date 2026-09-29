import sys
import os

# Add the backend directory to python path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.db import db
from app.core.config import settings

def clear_data():
    collection = db[settings.MONGO_COLLECTION_SALES]
    
    print(f"Borrando documentos de la colección '{settings.MONGO_COLLECTION_SALES}'...")
    result = collection.delete_many({})
    
    print(f"¡Éxito! Se eliminaron {result.deleted_count} transacciones.")

if __name__ == "__main__":
    print("⚠️  ADVERTENCIA: Esta acción eliminará todas las ventas de la base de datos.")
    respuesta = input("¿Estás seguro de continuar? (s/n): ")
    
    if respuesta.lower() == 's':
        clear_data()
    else:
        print("Operación cancelada. No se borró nada.")
