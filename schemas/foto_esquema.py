from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, BLOB
from config.db import motor

meta = MetaData()

fotos = Table('foto', meta,
              Column('idfoto', Integer, primary_key=True, autoincrement="auto"),
              Column('data', BLOB),
              Column('idReporte', Integer)
              )

motorBd = motor()
meta.create_all(motorBd)