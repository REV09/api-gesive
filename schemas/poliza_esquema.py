from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, Boolean
from config.db import motor

meta = MetaData()

polizas = Table('poliza', meta,
                Column('idpoliza', Integer, primary_key=True, autoincrement="auto"),
                Column('idConductor', Integer),
                Column('idVehiculo', Integer),
                Column('fechaInicio', Date),
                Column('plazo', Integer),
                Column('tipoCobertura', String(20)),
                Column('costo', Float),
                Column('fechaFin', Date))

motorBd = motor()
meta.create_all(motorBd)