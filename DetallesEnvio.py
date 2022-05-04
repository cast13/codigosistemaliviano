

class DetallesEnvio:
    IdEnvio=int
    IdProducto=int
    NombreProducto=str
    Cantidad=int
    CostoUnitario=float
    Subtotal=float

    def __init__(self,IdEnvio,IdProducto,NombreProducto,Cantidad,CostoUnitario,Subtotal):
        self._IdEnvio=IdEnvio
        self._IdProducto=IdProducto
        self._NombreProducto=NombreProducto
        self._Cantidad=Cantidad
        self._CostoUnitario=CostoUnitario
        self._Subtotal=Subtotal

    def CancelarEnvio(self):

    def PrecioTotal(self):
        