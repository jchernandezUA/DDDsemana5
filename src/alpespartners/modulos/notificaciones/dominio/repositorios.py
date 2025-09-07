# Propósito: Definir las interfaces (contratos) para los repositorios del dominio de notificaciones.

"""Interfaces para los repositorios del dominio de Notificaciones"""

from abc import ABC
from seedwork.dominio.repositorios import Repositorio

class RepositorioNotificaciones(Repositorio, ABC):
    """Interfaz del repositorio de Notificaciones."""
    ...

class RepositorioTransacciones(Repositorio, ABC):
    """Interfaz del repositorio de Transacciones (si fuera necesario gestionarlas independientemente)."""
    ...