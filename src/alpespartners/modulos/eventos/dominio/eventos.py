"""
Eventos de Dominio del módulo de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass
from seedwork.dominio.eventos import EventoDominio
from datetime import datetime
from uuid import UUID


@dataclass
class EventoCreado(EventoDominio):
    """
    Evento que se dispara cuando se crea un nuevo evento en el sistema
    """
    evento_id: UUID
    tipo: str
    fecha_creacion: datetime

    def nombre_evento(self) -> str:
        return "eventos.evento_creado"
