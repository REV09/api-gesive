from sqlalchemy import create_engine

from security.encriptacion import desencriptar_usuario, desencriptar_contrasena

USERBD = desencriptar_usuario()
PASSBD = desencriptar_contrasena()

def conexionDb():

    '''
    Este metodo retorna la conexion para la base de datos es un objeto
    de tipo Connection.
    Funciona usando el driver de mysql + pysqml recibe el usuario y la
    contraseña y despues el host de la bd, el puerto y la base de datos
    seleccionada por defecto, ademas para que la conexion funcione
    requiere usar un ssl
    '''

    motorBd = create_engine(f"mysql+pymysql://{USERBD}:{PASSBD}"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:40594/2d6206eac7c9", echo=True,   connect_args={'ssl': {'activate': True}})
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    Este metodo retorna un motor de interaccion con la base de datos
    utiliza el mismo metodo de conexion que el metod conexionDb
    la diferencia es que este solo retorna el motor de la base de
    datos.
    '''

    motorBd = create_engine(f"mysql+pymysql://{USERBD}:{PASSBD}"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:40594/2d6206eac7c9", echo=True,   connect_args={'ssl': {'activate': True}})
    return motorBd
