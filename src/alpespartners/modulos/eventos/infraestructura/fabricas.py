"""
Fábricas de infraestructura para el módulo de Eventos
"""
from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.eventos.dominio.repositorios import RepositorioEventos, RepositorioEventosIntegracion
from .repositorios import RepositorioEventosPostgreSQL
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


@dataclass
class FabricaRepositorio(Fabrica):
    """
    Fábrica para crear repositorios de eventos
    """

    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioEventos:
            return RepositorioEventosPostgreSQL()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion(f"No existe implementación para {obj}")

def obtener_fabrica_repositorio():
    """
    Obtiene la fábrica de repositorio según la configuración
    """
    # Por defecto, usar PostgreSQL
    return FabricaRepositorio()


