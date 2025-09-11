"""
DTOs del módulo de Eventos
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class EventoDTO:
    """DTO para transferencia de datos de eventos"""
    id: str
    tipo: str
    id_socio: UUID
    id_programa: UUID
    monto: float
    fecha_creacion: str
    fecha_procesamiento: Optional[str] = None