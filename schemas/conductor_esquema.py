from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Date
from config.db import motor

meta = MetaData()

conductores = Table('conductor', meta,
                    Column('idConductor', Integer, primary_key=True),
                    Column('nombreCompleto', String(90)),
                    Column('numLicencia', String(25)),
                    Column('fechaNacimiento', Date),
                    Column('telefono', String(15)),
                    Column('contrasena', String(20))
                    )

motorBd = motor()
meta.create_all(motor)