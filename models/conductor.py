from pydantic import BaseModel
from datetime import date


class Conductor(BaseModel):
    idconductor: int
    nombreCompleto: str
    numLicencia: str
    fechaNacimiento: date
    telefono: str
    contrasena: str

    class Config:
        orm_mode = True
