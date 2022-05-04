

class DetalleFactura:
    CodigoFactura=int
    CodigoProducto=int
    Cantidad=int
    Detalle=str
    Subtotal=float

    def __init__(self,CodigoFactura,CodigoProducto,Cantidad,Detalle,Subtotal):
        self.CodigoFactura=CodigoFactura
        self.CodigoProducto=CodigoProducto
        self.Cantidad=Cantidad
        self.Detalle=Detalle
        self.Subtotal=Subtotal

    def GenerarFactura(self):