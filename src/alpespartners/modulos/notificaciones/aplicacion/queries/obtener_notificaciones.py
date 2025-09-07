from seedwork.aplicacion.queries import Query
from modulos.notificaciones.aplicacion.dto import NotificacionDTO
from dataclasses import dataclass
from typing import List
from .base import NotificacionQueryBaseHandler
from modulos.notificaciones.infraestructura.repositorios import RepositorioNotificacionesSQLAlchemy

@dataclass
class ObtenerNotificaciones(Query):
    pass

class ObtenerNotificacionesHandler(NotificacionQueryBaseHandler):
    
    def handle(self, query: ObtenerNotificaciones) -> List[NotificacionDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioNotificacionesSQLAlchemy.__class__)
        notificaciones = repositorio.obtener_todos()
        return [self.fabrica_notificaciones.crear_objeto(notif, self.mapeador_notificacion) for notif in notificaciones]
