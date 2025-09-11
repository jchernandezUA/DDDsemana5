"""
Repositorios de infraestructura para el módulo de Eventos
"""
from typing import List, Optional
from uuid import UUID

from config.db import db
from modulos.eventos.dominio.repositorios import RepositorioEventos
from modulos.eventos.dominio.entidades import Evento
from modulos.eventos.dominio.fabricas import FabricaEventos

from .dto import EventoEntity
from .mapeadores import MapeadorEvento


class RepositorioEventosPostgreSQL(RepositorioEventos):
    """
    Implementación PostgreSQL del repositorio de eventos
    """

    def __init__(self):
        self._fabrica_eventos: FabricaEventos = FabricaEventos()
        self._mapeador: MapeadorEvento = MapeadorEvento()

    def obtener_por_id(self, evento_id: UUID) -> Optional[Evento]:
        evento_entity = db.session.query(EventoEntity).filter_by(id=evento_id).first()
        if not evento_entity:
            return None
        
        return self._mapeador.entity_a_entidad(evento_entity)

    def obtener_todos(self) -> List[Evento]:
        eventos_entity = db.session.query(EventoEntity).all()
        return [self._mapeador.entity_a_entidad(entity) for entity in eventos_entity]

    def agregar(self, evento: Evento) -> None:
        evento_entity = self._mapeador.entidad_a_entity(evento)
        db.session.add(evento_entity)