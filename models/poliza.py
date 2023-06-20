from pydantic import BaseModel
from datetime import datetime

class Poliza(BaseModel):
    idpoliza: int
    idConductor: int
    idVehiculo: int
    fechaInicio: datetime
    fechaFin: datetime
    plazo: int
    tipoCobertura: str
    costo: float

    class Config:
        orm_mode = True