from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, Boolean
from config.db import motor

meta = MetaData()

pagos = Table('pago', meta,
              Column('idPago', Integer, primary_key=True),
              Column('idPoliza', Integer),
              Column('idConductor', Integer),
              Column('monto', Float),
              Column('fecha', Date),
              Column('formaDePago', Boolean),
              Column('numeroTarjeta', String(24)),
              Column('fechaVencimiento', String(6)),
              Column('cvv', String(8)))

motorBd = motor()
meta.create_all(motorBd)