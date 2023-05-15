from sqlalchemy import create_engine

def conexionDb():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://S19014007:HALOcea206-"
                          + "@containers-us-west-135.railway.app:7712/railway")
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    '''
    motorBd = create_engine("mysql+pymysql://S19014007:HALOcea206-"
                          + "@containers-us-west-135.railway.app:7712/railway")
    return motorBd
