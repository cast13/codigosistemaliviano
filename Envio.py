


class Envio:
    IdProducto= int
    FechaOrden= str
    NombreCliente= str
    Estado= str
    Precio= float

    def __init__(self,IdProducto,FechaOrden,NombreCliente,Estado,Precio):
        self._IdProducto=IdProducto
        self._FechaOrden=FechaOrden
        self._NombreCliente=NombreCliente
        self._Estado=Estado
        self._Precio=Precio

    def RealizarEnvio(self):

    def ActualizarEnvio(self):

    def CancelarEnvio(self):        