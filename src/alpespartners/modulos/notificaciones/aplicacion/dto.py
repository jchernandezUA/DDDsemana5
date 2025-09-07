# Propósito: Definir los Data Transfer Objects (DTOs) que representan las notificaciones 
# en la capa de aplicación. Son los objetos que se mueven entre la API y los handlers.

from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ContenidoDTO(DTO):
    """DTO para el contenido de una notificación."""
    asunto: str
    cuerpo: str

@dataclass(frozen=True)
class NotificacionDTO(DTO):
    """DTO principal para la entidad de Notificación."""
    id: str = field(default_factory=str)
    destinatario_email: str = field(default_factory=str)
    tipo_notificacion: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    id_pago: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    contenido: ContenidoDTO = field(default_factory=ContenidoDTO)
