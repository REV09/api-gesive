from cryptography.fernet import Fernet

def generar_llave():
    
    llave = Fernet.generate_key()
    with open("SECRET.key", "wb") as key_file:
        key_file.write(llave)


def cargar_llave():

    return open("security/SECRET.key", "rb").read()


def encriptar_contenido(contenido: str, llave: bytes):

    contenido_codificado = contenido.encode()
    fernet_cripto = Fernet(llave)
    contenido_encriptado = fernet_cripto.encrypt(contenido_codificado)
    return contenido_encriptado


def desencriptar_contenido(contenido_encriptado: bytes, llave: bytes):

    fernet_cripto = Fernet(llave)
    contenido = fernet_cripto.decrypt(contenido_encriptado).decode()
    return contenido


def cargar_usuario():
     return open("security/USER.key", "rb").read()


def cargar_contrasena():
    return open("security/PASS.key", "rb").read()


def desencriptar_usuario():

    usuario_encriptado = cargar_usuario()
    llave = cargar_llave()
    usuario_desencriptado = desencriptar_contenido(usuario_encriptado, llave)
    return usuario_desencriptado


def desencriptar_contrasena():

    clave_encriptada = cargar_contrasena()
    llave = cargar_llave()
    clave_desencriptada = desencriptar_contenido(clave_encriptada, llave)
    return clave_desencriptada
