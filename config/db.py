from sqlalchemy import create_engine
import sqlalchemy
import ssl

def conexionDb():

    '''
    mysql+pymysql://76bcbcdd423c7195:3d9356e09f9e6290e0e874618db1d1@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:40594/2d6206eac7c9
    '''

    motorBd = create_engine("mysql+pymysql://apiuser:BDdsr198709-"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:40594/2d6206eac7c9", echo=True,   connect_args={'ssl': {'activate': True}})
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://apiuser:BDdsr198709-"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:40594/2d6206eac7c9", echo=True,   connect_args={'ssl': {'activate': True}})
    return motorBd
