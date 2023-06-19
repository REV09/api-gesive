from pydantic import BaseModel

from security.encriptacion import cargar_llave, desencriptar_contenido, encriptar_contenido

class Vehiculo(BaseModel):
    idvehiculo: int
    numeroSerie: str
    anio: int
    marca: str
    modelo: str
    color: str
    numPlacas: str
    idConductor: int

    class Config:
        orm_mode = True

    def codificar_informacion(self):
        llave = cargar_llave()
        self.numeroSerie = encriptar_contenido(self.numeroSerie, llave).decode()
        self.numPlacas = encriptar_contenido(self.numPlacas, llave).decode()


    def decodificar_informacion(self):
        llave = cargar_llave()
        self.numeroSerie = desencriptar_contenido(self.numeroSerie.encode(), llave)
        self.numPlacas = desencriptar_contenido(self.numPlacas.encode(), llave)