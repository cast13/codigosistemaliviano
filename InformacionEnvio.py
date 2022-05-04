

class InformacionEnvio:
    IdEnvio=int
    TipoEnvio=str
    CostoEnvio=int
    RegionEnvio=int

    def __init__(self,IdEnvio,TipoEnvio,CostoEnvio,RegionEnvio):
        self._IdEnvio=IdEnvio
        self._TipoEnvio=TipoEnvio
        self._CostoEnvio=CostoEnvio
        self._RegionEnvio=RegionEnvio

    def ActualizarInfoENvio(self):

        