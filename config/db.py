from sqlalchemy import create_engine


def conexionDb():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://e212849251743278:4f72da1965aec2f114e7b7c968e33a"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:3306/864c14fd73b9")
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://e212849251743278:4f72da1965aec2f114e7b7c968e33a"
                            "@primary.aseguradorabd--9x2lmpbqp2qf.addon.code.run:3306/864c14fd73b9")
    return motorBd
