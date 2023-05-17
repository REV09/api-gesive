from pydantic import BaseModel
from datetime import date

class Poliza(BaseModel):
    idPoliza: int
    idConductor: int
    idVehiculo: int
    fechaInicio: date
    fechaFin: date
    plazo: int
    tipoCobertura: str
    costo: float

    class Config:
        orm_mode = True