from sqlalchemy import create_engine


def conexionDb():

    '''
    '''
    
    

    motorBd = create_engine("mysql+pymysql://feb6d7bbd2f2cd28:2efc9bdc4a639713c2340dff6d646b"
                            "@primary.aseguradorabd--nymsp5vnyqbc.addon.code.run:3306/48d55fbbf1c5")
    conexion = motorBd.connect()
    return conexion


def motor():

    '''
    '''

    motorBd = create_engine("mysql+pymysql://feb6d7bbd2f2cd28:2efc9bdc4a639713c2340dff6d646b"
                            "@primary.aseguradorabd--nymsp5vnyqbc.addon.code.run:3306/48d55fbbf1c5")
    return motorBd
