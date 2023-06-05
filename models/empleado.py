from pydantic import BaseModel

class Empleado(BaseModel):
    idEmpleado: int
    nombreCompleto: str
    fechaIngreso: str
    cargo: str
    nombreUsuario: str
    contrasena: str

    class Config:
        orm_mode = True