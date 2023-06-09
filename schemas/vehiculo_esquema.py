from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import motor

meta = MetaData()

vehiculos = Table('vehiculo', meta,
                  Column('idvehiculo', Integer, primary_key=True),
                  Column('numeroSerie', String(255)),
                  Column('anio', Integer),
                  Column('marca', String(20)), 
                  Column('modelo', String(20)),
                  Column('color', String(20)),
                  Column('numPlacas', String(255))) 

motorBd = motor()
meta.create_all(motorBd)