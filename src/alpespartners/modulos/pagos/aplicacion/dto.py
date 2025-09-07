# Propósito: Definir los Data Transfer Objects (DTOs) que representan los pagos y sus componentes 
# en la capa de aplicación. Son los objetos que se mueven entre la API y los handlers.

from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ComisionDTO(DTO):
    """DTO para una comisión individual dentro de un pago."""
    id_referencia: str
    monto: float
    moneda: str
    descripcion: str

@dataclass(frozen=True)
class PagoDTO(DTO):
    """DTO principal para la entidad de Pago."""
    id: str = field(default_factory=str)
    id_socio: str = field(default_factory=str)
    monto_total: float = field(default_factory=float)
    moneda: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    comisiones: list[ComisionDTO] = field(default_factory=list)