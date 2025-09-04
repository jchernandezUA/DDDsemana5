# Propósito: Definir todos los eventos de dominio que pueden ocurrir dentro del agregado Pago.

from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class PagoCreado(EventoDominio):
    pago_id: uuid.UUID = None
    id_socio: uuid.UUID = None
    monto_total: float = None
    moneda: str = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class PagoProcesado(EventoDominio):
    pago_id: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class PagoRechazado(EventoDominio):
    pago_id: uuid.UUID = None
    fecha_actualizacion: datetime = None
    motivo: str = None