
class Administrador(Usuario):

    NombreAdministrador=str
    Email:str


    def __init__(self,NombreAdministrador,Email):
        super().__init__(Id,Contraseña,EstadoRegistro,FechaRegistro)
        self._NombreAdministrador=NombreAdministrador
        self._Email=Email

    def ModificarProducto(self):