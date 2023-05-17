from pydantic import BaseModel
from datetime import date

class Empleado(BaseModel):
    idEmpleado: int
    nombreCompleto: str
    fechaIngreso: date
    cargo: str
    nombreUsuario: str
    contrasena: str

    class Config:
        orm_mode = True