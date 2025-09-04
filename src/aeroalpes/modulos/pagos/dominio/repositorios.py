# Propósito: Definir las interfaces (contratos) para los repositorios del dominio de pagos.

"""Interfaces para los repositorios del dominio de Pagos"""

from abc import ABC
from aeroalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioPagos(Repositorio, ABC):
    """Interfaz del repositorio de Pagos."""
    ...

class RepositorioTransacciones(Repositorio, ABC):
    """Interfaz del repositorio de Transacciones (si fuera necesario gestionarlas independientemente)."""
    ...