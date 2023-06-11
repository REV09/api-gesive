from pydantic import BaseModel
from datetime import date

from security.encriptacion import cargar_llave, desencriptar_contenido, encriptar_contenido


class Reporte(BaseModel):
    idReporte: int
    idPoliza: int
    posicionLat: float
    posicionLon: float
    involucradosNombres: str
    involucradosVehiculos: str
    fotos: str
    idAjustador: int
    estatus: str
    dictamenTexto: str
    dictamenFecha: date
    dictamenHora: str
    dictamenFolio: str

    class Config:
        orm_mode = True

    def codificar_informacion(self):
        llave = cargar_llave()
        self.involucradosNombres = encriptar_contenido(self.involucradosNombres, llave).decode()
        self.involucradosVehiculos = encriptar_contenido(self.involucradosVehiculos, llave).decode()


    def decodificar_informacion(self):
        llave = cargar_llave()
        self.involucradosNombres = desencriptar_contenido(self.involucradosNombres.encode(), llave)
        self.involucradosVehiculos = desencriptar_contenido(self.involucradosVehiculos.encode(), llave)