from pydantic import BaseModel
from datetime import date


class Reporte(BaseModel):
    idReporte: int
    posicionLat: float
    posicionLon: float
    involucradosNombres: str
    involucradosVehiculos: str
    fotos: int
    idAjustador: int
    estatus: str
    dictamenTexto: str
    dictamenFecha: date
    dictamenHora: str
    dictamenFolio: str