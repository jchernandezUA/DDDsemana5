"""
Repositorios de infraestructura para el módulo de Eventos
"""
from typing import List, Optional
from uuid import UUID

from modulos.eventos.aplicacion.dto import EventoDTO
from config.db import db
from modulos.eventos.dominio.repositorios import RepositorioEventos
from modulos.eventos.dominio.entidades import Evento
from modulos.eventos.dominio.fabricas import FabricaEventos

from .dto import EventoEntity
from .mapeadores import MapeadorEvento


class RepositorioEventosPostgreSQL(RepositorioEventos):
    def __init__(self):
        self._fabrica_eventos: FabricaEventos = FabricaEventos()

    @property
    def fabrica_eventos(self):
        return self._fabrica_eventos

    def obtener_por_id(self, id: UUID) -> Evento:
        evento_dto = db.session.query(EventoDTO).filter_by(id=str(id)).one()
        return self.fabrica_eventos.crear_objeto(evento_dto, MapeadorEvento())

    def obtener_todos(self) -> list[Evento]:
        # Implementar lógica para obtener todos si es necesario
        raise NotImplementedError

    def agregar(self, evento: Evento):
        evento_dto = self.fabrica_eventos.crear_objeto(evento, MapeadorEvento())
        db.session.add(evento_dto)

    def actualizar(self, evento: Evento):
        evento_dto = self.fabrica_eventos.crear_objeto(evento, MapeadorEvento())
        db.session.merge(evento_dto) # Merge para actualizar

    def eliminar(self, evento_id: UUID):
        # Implementar lógica de eliminación si es necesario
        raise NotImplementedError