from models.conductor import Conductor
from datetime import datetime

conductor = Conductor(idconductor=1, nombreCompleto="Hector David Madrid Rivera",
                      numLicencia=1, fechaNacimiento=datetime.now(), telefono="2282334994", contrasena="HALOcea206-")

print(f"id de conductor: {conductor.idconductor}")
print(f"Nombre: {conductor.nombreCompleto}")
print(f"numero de licencia: {conductor.numLicencia}")
print(f"fecha de nacimiento: {conductor.fechaNacimiento}")
print(f"telefono: {conductor.telefono}")
print(f"contraseña: {conductor.contrasena}")

conductor.codificar_informacion()
print("- - - - - - - - - - - - - - - - - - - - - -")

print(f"id de conductor: {conductor.idconductor}")
print(f"Nombre: {conductor.nombreCompleto}")
print(f"numero de licencia: {conductor.numLicencia}")
print(f"fecha de nacimiento: {conductor.fechaNacimiento}")
print(f"telefono: {conductor.telefono}")
print(f"contraseña: {conductor.contrasena}")

conductor.decodificar_informacion()
print("- - - - - - - - - - - - - - - - - - - - - -")

print(f"id de conductor: {conductor.idconductor}")
print(f"Nombre: {conductor.nombreCompleto}")
print(f"numero de licencia: {conductor.numLicencia}")
print(f"fecha de nacimiento: {conductor.fechaNacimiento}")
print(f"telefono: {conductor.telefono}")
print(f"contraseña: {conductor.contrasena}")