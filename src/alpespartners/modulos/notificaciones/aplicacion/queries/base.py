from seedwork.aplicacion.queries import QueryHandler
from modulos.notificaciones.infraestructura.fabricas import FabricaRepositorio, FabricaNotificaciones
from modulos.notificaciones.aplicacion.mapeadores import MapeadorNotificacion

class NotificacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorio()
        self._fabrica_notificaciones = FabricaNotificaciones()
        self._mapeador_notificacion = MapeadorNotificacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property 
    def fabrica_notificaciones(self):
        return self._fabrica_notificaciones
        
    @property
    def mapeador_notificacion(self):
        return self._mapeador_notificacion
