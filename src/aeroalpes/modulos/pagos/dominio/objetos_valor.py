# Propósito: Definir los objetos valor que encapsulan conceptos y reglas 
# inmutables del dominio de pagos.

from __future__ import annotations
from dataclasses import dataclass
# Asegúrate de importar ObjetoValor del seedwork
from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor
from enum import Enum
import uuid # Importa uuid

@dataclass(frozen=True)
class Monto(ObjetoValor):
    valor: float
    moneda: str

    def es_positivo(self) -> bool:
        """Verifica si el valor del monto es mayor que cero."""
        return self.valor > 0

class EstadoPago(str, Enum):
    PENDIENTE = "Pendiente"
    PROCESADO = "Procesado"
    RECHAZADO = "Rechazado"

# ========== CORRIGE ESTA CLASE ==========
@dataclass(frozen=True)
class IdSocio(ObjetoValor):
    """Representa el identificador único de un socio."""
    valor: uuid.UUID # Usamos el tipo UUID para mayor robustez
# ======================================