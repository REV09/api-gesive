from pydantic import BaseModel

from security.encriptacion import cargar_llave, desencriptar_contenido, encriptar_contenido


class Empleado(BaseModel):
    idEmpleado: int
    nombreCompleto: str
    fechaIngreso: str
    cargo: str
    nombreUsuario: str
    contrasena: str

    def codificar_informacion(self):
        llave = cargar_llave()
        self.nombreCompleto = encriptar_contenido(
            self.nombreCompleto, llave).decode()
        self.contrasena = encriptar_contenido(self.contrasena, llave).decode()

    def decodificar_informacion(self):
        llave = cargar_llave()
        self.nombreCompleto = desencriptar_contenido(
            self.nombreCompleto.encode(), llave)
        self.contrasena = desencriptar_contenido(
            self.contrasena.encode(), llave)

    class Config:
        orm_mode = True
