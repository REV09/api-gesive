from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import String, Integer, Date
from config.db import motor

meta = MetaData()

empleados = Table('empleado', meta,
                  Column('idEmpleado', Integer, primary_key=True),
                  Column('nombreCompleto', String(45),),
                  Column('fechaIngreso', Date,),
                  Column('cargo', String(10),),
                  Column('nombreUsuario', String(15),),
                  Column('contrasena', String(90),))

motorBd = motor()
meta.create_all(motorBd)