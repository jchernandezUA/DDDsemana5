"""
Eventos de Dominio del módulo de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.eventos import EventoDominio
from datetime import datetime
from uuid import UUID


@dataclass
class EventoCreado(EventoDominio):
    """
    Evento que se dispara cuando se crea un nuevo evento en el sistema
    """
    evento_id: UUID = field(default=None)
    tipo: str = field(default="")
    fecha_creacion: datetime = field(default_factory=datetime.now)

    def nombre_evento(self) -> str:
        return "eventos.evento_creado"
