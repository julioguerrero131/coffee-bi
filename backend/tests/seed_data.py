import sys
import os
from datetime import datetime, timedelta
import random

# Add the backend directory to python path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.db import db
from app.core.config import settings

def seed_data():
    collection = db[settings.MONGO_COLLECTION_SALES]
    
    # Optional: Clear existing data to start fresh (uncomment if desired)
    # collection.delete_many({})
    
    sucursales = ["Sur", "Centro", "Norte"]
    metodos_pago = ["Tarjeta", "Efectivo", "Transferencia"]
    
    productos = [
        {"nombre": "Cappuccino Grande", "categoria": "Bebidas Calientes", "precio": 4.5},
        {"nombre": "Latte Vainilla", "categoria": "Bebidas Calientes", "precio": 4.0},
        {"nombre": "Espresso Doble", "categoria": "Bebidas Calientes", "precio": 3.0},
        {"nombre": "Frappé Mocca", "categoria": "Bebidas Frías", "precio": 5.5},
        {"nombre": "Té Helado", "categoria": "Bebidas Frías", "precio": 3.5},
        {"nombre": "Muffin de Arándanos", "categoria": "Alimentos", "precio": 3.0},
        {"nombre": "Croissant", "categoria": "Alimentos", "precio": 2.5},
        {"nombre": "Galleta con Chispas", "categoria": "Alimentos", "precio": 2.0},
    ]
    
    sales = []
    # Comenzar desde el inicio del 2024
    current_date = datetime(2024, 1, 1, 8, 0, 0)
    
    print("Generando 50 ventas de prueba secuenciales desde 2024 a 2026...")
    
    for i in range(1, 51):
        producto = random.choice(productos)
        
        # TK-1001, TK-1002...
        ticket_id = f"TK-{1000 + i}"
        
        # Incrementar la fecha actual sumándole días y horas de forma aleatoria
        # para esparcir 50 registros a lo largo de 3 años (2024-2026)
        # 3 años = ~1095 días, 1095 / 50 = ~22 días de diferencia entre cada ticket
        current_date += timedelta(days=random.randint(15, 28), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        
        sale = {
            "id_ticket": ticket_id,
            "fecha_hora": current_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "producto": producto["nombre"],
            "categoria": producto["categoria"],
            "monto": producto["precio"],
            "metodo_pago": random.choice(metodos_pago),
            "sucursal": random.choice(sucursales)
        }
        
        sales.append(sale)
    
    # Insert into MongoDB
    if sales:
        result = collection.insert_many(sales)
        print(f"¡Éxito! Se insertaron {len(result.inserted_ids)} transacciones.")
        print(f"Colección usada: {settings.MONGO_COLLECTION_SALES}")
    else:
        print("No se generaron ventas.")

if __name__ == "__main__":
    seed_data()
