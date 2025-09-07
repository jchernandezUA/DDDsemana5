# Propósito: Implementación concreta del repositorio de notificaciones usando SQLAlchemy.

from config.db import db
from modulos.notificaciones.dominio.repositorios import RepositorioNotificaciones
from modulos.notificaciones.dominio.entidades import Notificacion
from modulos.notificaciones.infraestructura.dto import Notificacion as NotificacionDTO
from modulos.notificaciones.infraestructura.mapeadores import MapeadorNotificacion

class RepositorioNotificacionesSQLAlchemy(RepositorioNotificaciones):

    def __init__(self):
        self._fabrica_notificaciones = MapeadorNotificacion()

    @property
    def fabrica_notificaciones(self):
        return self._fabrica_notificaciones

    def obtener_por_id(self, id: str) -> Notificacion:
        notificacion_dto = db.session.query(NotificacionDTO).filter_by(id=id).one()
        return self.fabrica_notificaciones.entidad_a_dto(notificacion_dto)

    def agregar(self, notificacion: Notificacion):
        notificacion_dto = self.fabrica_notificaciones.entidad_a_dto(notificacion)
        db.session.add(notificacion_dto)

    def actualizar(self, notificacion: Notificacion):
        notificacion_dto = self.fabrica_notificaciones.entidad_a_dto(notificacion)
        db.session.merge(notificacion_dto)

    def eliminar(self, id: str):
        notificacion_dto = db.session.query(NotificacionDTO).filter_by(id=id).one()
        db.session.delete(notificacion_dto)
