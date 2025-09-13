"""
Eventos de Dominio del módulo de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.eventos import EventoDominio
from datetime import datetime
from uuid import UUID


@dataclass
class EventoRegistrado(EventoDominio):
    """
    Evento que se dispara cuando se crea un nuevo evento en el sistema
    """
    evento_id: UUID = field(default=None)
    tipo_evento: str = field(default="")
    id_referido: UUID = field(default=None)
    id_socio: UUID = field(default=None)
    monto: float = field(default=0.0)
    estado: str = field(default="pendiente")
    fecha_evento: datetime = field(default_factory=datetime.now)

    def nombre_evento(self) -> str:
        return "eventos.eventos-tracking"
