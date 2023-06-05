from cryptography.fernet import Fernet

def generar_llave():

    '''
    Este metodo es el encargado de crear la llave de encriptacion
    utilizada por JWT
    '''
    
    llave = Fernet.generate_key()
    with open("SECRET.key", "wb") as key_file:
        key_file.write(llave)


def cargar_llave():

    '''
    Este metodo es el encargado de cargar la llave de seguridad
    utilizado por JWT y tambien se utiliza para el cifrado de
    informacion sensible en la base de datos.
    '''

    return open("security/SECRET.key", "rb").read()


def encriptar_contenido(contenido: str, llave: bytes):

    '''
    Este metodo es el encargado de cifrar un contenido especifico
    el argumento contenido recibe la informacion que se debe cifrar
    mientras que el argumento llave recibe la llave con la que se
    va a cifrar la informacion.
    Para su funcionamiento el contenido primero debe ser convertido
    en un objeto de tipo bytes, despues de eso se procede al cifrado.
    
    El metodo retorna el contenido encriptado como un objeto de tipo
    bytes
    '''

    contenido_codificado = contenido.encode()
    fernet_cripto = Fernet(llave)
    contenido_encriptado = fernet_cripto.encrypt(contenido_codificado)
    return contenido_encriptado


def desencriptar_contenido(contenido_encriptado: bytes, llave: bytes):

    '''
    Este metodo se usa para el desencriptado de un contenido
    especificado en el argumento contenido_encriptado el cual es un
    objeto de tipo bytes, ademas de recibir la llave de cifrado en
    el argumento llave que tambien es un objeto de tipo bytes.

    El metodo retorna el contenido ya desencriptado como una cadena
    de texto plano, para eso al final del metodo decrypt se usa el
    metodo decode que se encarga de quitar el formato de bytes y
    convertirlo ya en texto plano.
    '''

    fernet_cripto = Fernet(llave)
    contenido = fernet_cripto.decrypt(contenido_encriptado).decode()
    return contenido


def cargar_usuario():
     
    '''
    Este metodo se encarga de cargar el usuario de conexion para la
    base de datos que se encuentra cifrado en el archivo 
    especificado en el metodo, es retornado como un objeto de tipo
    bytes.
    '''

    return open("security/USER.key", "rb").read()


def cargar_contrasena():

    '''
    Este metodo se encarga de cargar la contraseña de conexion para
    la base de datos que se encuentra cifrado en el archivo
    especificado en el metodo, es retornado como un objeto de tipo
    bytes.
    '''

    return open("security/PASS.key", "rb").read()


def desencriptar_usuario():

    '''
    Este metodo se encarga de desencriptar el usuario codificado para
    la conexion de la base de datos y retorna el usuario
    desencriptado listo para ser leido mediante la conexion de la 
    base de datos.
    '''

    usuario_encriptado = cargar_usuario()
    llave = cargar_llave()
    usuario_desencriptado = desencriptar_contenido(usuario_encriptado, llave)
    return usuario_desencriptado


def desencriptar_contrasena():

    '''
    Este metodo se encarga de desencriptar la contraseña codificado 
    para la conexion de la base de datos y retorna la contraseña
    desencriptada listo para ser leido mediante la conexion de la 
    base de datos.
    '''

    clave_encriptada = cargar_contrasena()
    llave = cargar_llave()
    clave_desencriptada = desencriptar_contenido(clave_encriptada, llave)
    return clave_desencriptada
