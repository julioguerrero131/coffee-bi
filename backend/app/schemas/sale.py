from pydantic import BaseModel
from datetime import datetime

class Sale(BaseModel):
    id_ticket: str
    fecha_hora: datetime
    producto: str
    categoria: str
    monto: float
    metodo_pago: str
    sucursal: str
