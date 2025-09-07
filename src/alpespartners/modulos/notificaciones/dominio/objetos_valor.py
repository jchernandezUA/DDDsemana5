# Propósito: Definir los objetos valor que encapsulan conceptos y reglas 
# inmutables del dominio de notificaciones.

from __future__ import annotations
from dataclasses import dataclass
from seedwork.dominio.objetos_valor import ObjetoValor
from enum import Enum
import uuid

@dataclass(frozen=True)
class DestinatarioEmail(ObjetoValor):
    """Representa el email del destinatario de la notificación."""
    valor: str

    def es_valido(self) -> bool:
        """Verifica si el email tiene un formato válido básico."""
        return "@" in self.valor and "." in self.valor

class TipoNotificacion(str, Enum):
    PAGO_CREADO = "Pago Creado"
    PAGO_PROCESADO = "Pago Procesado"
    PAGO_RECHAZADO = "Pago Rechazado"

class EstadoNotificacion(str, Enum):
    PENDIENTE = "Pendiente"
    ENVIADA = "Enviada"
    FALLIDA = "Fallida"

@dataclass(frozen=True)
class ContenidoNotificacion(ObjetoValor):
    """Representa el contenido de la notificación."""
    asunto: str
    cuerpo: str

    def es_valido(self) -> bool:
        """Verifica si el contenido tiene asunto y cuerpo."""
        return bool(self.asunto.strip()) and bool(self.cuerpo.strip())

@dataclass(frozen=True)
class IdPago(ObjetoValor):
    """Representa el identificador único de un pago."""
    valor: uuid.UUID
