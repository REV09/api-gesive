from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date
from config.db import motor

meta = MetaData()

reportes = Table('reporte', meta,
                 Column('idReporte', Integer, primary_key=True),
                 Column('posicionLat', Float),
                 Column('posicionLon', Float),
                 Column('involucradosNombres', String(45)),
                 Column('involucradosVehiculos', String(45)),
                 Column('fotos', Integer),
                 Column('idAjustador', Integer),
                 Column('estatus', String(45)),
                 Column('dictamenTexto', String(45)),
                 Column('dictamenFecha', Date),
                 Column('dictamenHora', String(45)),
                 Column('dictamenFolio', String(45)))

motorBd =motor()
meta.create_all(motorBd)