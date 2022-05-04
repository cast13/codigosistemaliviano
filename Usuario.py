from sqlite3 import Date


class Usuario:

    Id=str
    Contraseña=str
    EstadoRegistro=str
    FechaRegistro= Date


    def __init__(self,Id,Contraseña,EstadoRegistro,FechaRegistro):
        self._Id=Id
        self._Contraseña=Contraseña
        self._EstadoRegistro=EstadoRegistro
        self._FechaRegistro=FechaRegistro

    def VerificarSesion(self):
        if Usuario:
            self.UsuarioCorrecto=True
            print("Su usuario es correcto {}".format(self.UsuarioCorrecto))

        else:
            print("Usuario incorrecto")

Id=input("Introduzaca el nuevo usuario que desea tener: ")
Contraseña=input("introduzca su contraseña: ")
EstadoRegistro=input("Activo")
FechaRegistro=Date


t=Usuario(Id,Contraseña,EstadoRegistro,FechaRegistro)
t.VerificarSesion()








