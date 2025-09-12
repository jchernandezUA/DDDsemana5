"""
Entidades del dominio de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.entidades import AgregacionRaiz
from .objetos_valor import TipoEvento
from .eventos import EventoCreado
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


@dataclass
class Evento(AgregacionRaiz):
    """
    Entidad principal que representa un evento en el sistema
    """
    tipo: TipoEvento = field(default=None)
    id_socio: UUID = field(default=None)
    id_programa: UUID = field(default=None)
    monto: float = field(default=0.0)
    fecha_creacion: datetime = field(default_factory=datetime.utcnow)
    fecha_procesamiento: Optional[datetime] = field(default=None)

    def crear_evento(self, evento: Evento):
        """
        Método para iniciar la creación del agregado.
        Dispara el evento de dominio inicial.
        """
        self.tipo = evento.tipo
        self.id_socio = evento.id_socio
        self.id_programa = evento.id_programa
        self.monto = evento.monto
        self.fecha_creacion = evento.fecha_creacion
        self.fecha_procesamiento = evento.fecha_procesamiento

        self.agregar_evento(EventoCreado(
            evento_id=self.id,
            tipo=self.tipo.valor,
            fecha_creacion=self.fecha_creacion
        ))
