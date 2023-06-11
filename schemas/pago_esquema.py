from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, Boolean
from config.db import motor

meta = MetaData()

pagos = Table('pago', meta,
              Column('idPago', Integer, primary_key=True, autoincrement="auto"),
              Column('idPoliza', Integer),
              Column('idConductor', Integer),
              Column('monto', Float),
              Column('fecha', Date),
              Column('formaDePago', Boolean),
              Column('numeroTarjeta', String(255)), 
              Column('fechaVencimiento', String(255)), 
              Column('cvv', String(255)))

motorBd = motor()
meta.create_all(motorBd)