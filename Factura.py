

from sqlite3 import Date
from tokenize import Double


class Factura:
    CodigoFactura=int
    Fecha= Date
    Total= float

    def __init__(self,CodigoFactura,Fecha,Total):
        self.CodigoFactura=CodigoFactura
        self.Fecha=Fecha
        self.Total=Total
    
    def GenerarFactura(self):
        
