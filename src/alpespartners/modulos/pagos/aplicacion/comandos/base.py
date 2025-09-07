# Propósito: Clase base para los handlers de comandos de pagos, para 
# inyectar dependencias comunes.

from seedwork.aplicacion.comandos import ComandoHandler
from modulos.pagos.infraestructura.fabricas import FabricaRepositorio
from modulos.pagos.dominio.fabricas import FabricaPagos

class PagoBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_pagos: FabricaPagos = FabricaPagos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_pagos(self):
        return self._fabrica_pagos