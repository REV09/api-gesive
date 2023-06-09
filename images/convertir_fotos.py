from models.foto import Foto

def obtener_binarios_fotos():
    with open("images/auto 1.jpeg", "rb") as foto:
        blob = foto.read()

    return blob

def crear_foto(datos_foto: bytes):
    foto_bd = Foto(idfoto=0, data=datos_foto, idReporte=1)
    return foto_bd


def guardar_foto(foto_recibida):
    with open("images/foto.jpeg", "wb") as foto:
        foto.write(foto_recibida)

def leer_foto():
    with open("images/foto.jpeg", "rb") as foto:
        blob = foto.read()

    return blob