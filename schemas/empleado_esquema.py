from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Date
from config.db import motor

meta = MetaData()

empleados = Table('empleado', meta,
                  Column('idEmpleado', Integer, primary_key=True),
                  Column('nombreCompleto', String(255),),
                  Column('fechaIngreso', String(10),),
                  Column('cargo', String(255),), 
                  Column('nombreUsuario', String(255),), 
                  Column('contrasena', String(255),)) 

motorBd = motor()
meta.create_all(motorBd)