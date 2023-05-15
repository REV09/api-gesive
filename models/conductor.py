from pydantic import BaseModel
import datetime


class Conductor(BaseModel):
    idConductor: int
    nombreCompleto: str
    numLicencia: str
    fechaNacimiento: datetime
    telefono: str
    contrasena: str
