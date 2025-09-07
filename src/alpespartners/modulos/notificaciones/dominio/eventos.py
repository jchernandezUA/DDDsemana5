# Propósito: Definir todos los eventos de dominio que pueden ocurrir dentro del agregado Notificacion.

from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class NotificacionCreada(EventoDominio):
    notificacion_id: uuid.UUID = None
    destinatario_email: str = None
    tipo_notificacion: str = None
    asunto: str = None
    cuerpo: str = None
    id_pago: uuid.UUID = None
    fecha_creacion: datetime = None

@dataclass
class NotificacionEnviada(EventoDominio):
    notificacion_id: uuid.UUID = None
    destinatario_email: str = None
    fecha_envio: datetime = None

@dataclass
class NotificacionFallida(EventoDominio):
    notificacion_id: uuid.UUID = None
    destinatario_email: str = None
    motivo_falla: str = None
    fecha_falla: datetime = None
