


from datetime import date
from sqlite3 import Date


class Cotizacion:
    IdCotizacion= int
    Detalles=str
    FechaCotizacion= Date

    def __init__(self,IdCotizacion,Detalles,FechaCotizacion):
        self.IdCotizacion=IdCotizacion
        self.Detalles=Detalles
        self.FechaCotizacion=FechaCotizacion

    def AplicaDescuentos(self):

    def EnviaCotizacion(self):

    def Imprimir(self):

    def CalcularCotizacion(self):