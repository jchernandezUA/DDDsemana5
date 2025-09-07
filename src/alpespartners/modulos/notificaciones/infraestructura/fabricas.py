# Propósito: Fábrica para crear repositorios de notificaciones.

from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.notificaciones.dominio.repositorios import RepositorioNotificaciones
from modulos.notificaciones.infraestructura.repositorios import RepositorioNotificacionesSQLAlchemy
from modulos.notificaciones.infraestructura.excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioNotificaciones:
            return RepositorioNotificacionesSQLAlchemy()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()
