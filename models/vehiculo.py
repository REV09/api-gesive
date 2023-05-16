from pydantic import BaseModel

class Vehiculo(BaseModel):
    idVehiculo: int
    numeroSerie: str
    anio: int
    marca: str
    modelo: str
    color: str
    numPlacas: str

    class Config:
        orm_mode = True