from Usuario import Usuario

class Cliente(Usuario):

    NombreCliente= str
    Direccion= str
    Email=str
    DatosEnvio= str
    Telefono= str


    def __init__(self,NombreCliente,Direccion,Email,DatoEnvio,Telefono):
        super().__init__(Id,Contraseña,EstadoRegistro,FechaRegistro)
        self._NombreCliente=NombreCliente
        self._Direccion=Direccion
        self._Email=Email
        self._DatoEnvio=DatoEnvio
        self._Telefono=Telefono

    def Registrarse(self):


    def ModificarPerfil(self):


    def ConsultaCotizacion(self):
