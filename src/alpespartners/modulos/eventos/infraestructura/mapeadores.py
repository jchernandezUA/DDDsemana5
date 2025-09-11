"""
Mapeadores para el módulo de Eventos
"""
import uuid
from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from alpespartners.modulos.eventos.aplicacion.dto import EventoDTO
from modulos.eventos.dominio.entidades import Evento
from modulos.eventos.dominio.objetos_valor import TipoEvento, EstadoEvento, MetadatosEvento, PrioridadEvento
from .dto import EventoEntity
from seedwork.dominio.repositorios import Mapeador
from datetime import datetime
import json


class MapeadorEventoDTOJson(AppMap):
    ...

class MapeadorEvento(RepMap):
    ...