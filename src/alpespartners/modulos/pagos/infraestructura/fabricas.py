# Propósito: Fábrica que crea la implementación concreta del repositorio.

from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.pagos.dominio.repositorios import RepositorioPagos
from .repositorios import RepositorioPagosPostgreSQL
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPagos.__class__:
            return RepositorioPagosPostgreSQL()
        else:
            # Ahora usamos la excepción específica que acabamos de definir
            raise NoExisteImplementacionParaTipoFabricaExcepcion()