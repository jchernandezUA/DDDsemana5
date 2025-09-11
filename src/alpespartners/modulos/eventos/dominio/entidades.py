"""
Entidades del dominio de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.entidades import AgregacionRaiz
from seedwork.dominio.objetos_valor import ObjetoValor
from .objetos_valor import TipoEvento, EstadoEvento, MetadatosEvento
from .eventos import EventoCreado, EventoProcesado, EventoFallido
from datetime import datetime
from uuid import UUID, uuid4
from typing import List, Optional


@dataclass
class Evento(AgregacionRaiz):
    """
    Entidad principal que representa un evento en el sistema
    """
    id: UUID = field(default_factory=uuid4)
    tipo: TipoEvento = field(default=None)
    id_socio: UUID = field(default=None)
    id_programa: UUID = field(default=None)
    monto: float = field(default=0.0)
    fecha_creacion: datetime = field(default_factory=datetime.utcnow)
    fecha_procesamiento: Optional[datetime] = field(default=None)

    def __post_init__(self):
        if not self.tipo:
            raise ValueError("El tipo de evento es obligatorio")
        
        # Agregar evento de dominio cuando se crea
        self.agregar_evento(EventoCreado(
            evento_id=self.id,
            tipo=self.tipo.valor,
            fecha_creacion=self.fecha_creacion
        ))
