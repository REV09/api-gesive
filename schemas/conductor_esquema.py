from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Date
from config.db import motor

meta = MetaData()

conductores = Table('conductor', meta,
                    Column('idconductor', Integer, primary_key=True, autoincrement="auto"),
                    Column('nombreCompleto', String(255)),
                    Column('numLicencia', String(255)), 
                    Column('fechaNacimiento', String(15)),
                    Column('telefono', String(255)), 
                    Column('contrasena', String(255)) 
                    )

motorBd = motor()
meta.create_all(motorBd)