from pydantic import BaseModel
from datetime import date
from security.encriptacion import cargar_llave, encriptar_contenido, desencriptar_contenido


class Conductor(BaseModel):
    idconductor: int
    nombreCompleto: str
    numLicencia: str
    fechaNacimiento: date
    telefono: str
    contrasena: str

    class Config:
        orm_mode = True

    def codificar_informacion(self):
        llave = cargar_llave()
        self.nombreCompleto = encriptar_contenido(self.nombreCompleto, llave).decode()
        self.numLicencia = encriptar_contenido(self.numLicencia, llave).decode()
        self.telefono = encriptar_contenido(self.telefono, llave).decode()
        self.contrasena = encriptar_contenido(self.contrasena, llave).decode()


    def decodificar_informacion(self):
        llave = cargar_llave()
        self.nombreCompleto = desencriptar_contenido(self.nombreCompleto.encode(), llave)
        self.numLicencia = desencriptar_contenido(self.numLicencia.encode(), llave)
        self.telefono = desencriptar_contenido(self.telefono.encode(), llave)
        self.contrasena = desencriptar_contenido(self.contrasena.encode(), llave)
