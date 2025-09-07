from seedwork.aplicacion.queries import Query
from modulos.notificaciones.aplicacion.dto import NotificacionDTO
from dataclasses import dataclass
from .base import NotificacionQueryBaseHandler
from modulos.notificaciones.infraestructura.repositorios import RepositorioNotificacionesSQLAlchemy

@dataclass
class ObtenerNotificacion(Query):
    id: str

class ObtenerNotificacionHandler(NotificacionQueryBaseHandler):
    
    def handle(self, query: ObtenerNotificacion) -> NotificacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioNotificacionesSQLAlchemy.__class__)
        notificacion = repositorio.obtener_por_id(query.id)
        return self.fabrica_notificaciones.crear_objeto(notificacion, self.mapeador_notificacion)
