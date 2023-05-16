from sqlalchemy import create_engine

def conexionDb():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://root:KUoC9YHQGLWeKOwS5DhQ"
                          + "@containers-us-west-135.railway.app:7712/railway")
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    '''
    motorBd = create_engine("mysql+pymysql://root:KUoC9YHQGLWeKOwS5DhQ"
                          + "@containers-us-west-135.railway.app:7712/railway")
    return motorBd
