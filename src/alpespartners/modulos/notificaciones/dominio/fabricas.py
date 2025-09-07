# Propósito: Crear el agregado Pago de forma segura, aplicando las reglas de negocio definidas.

"""Fábricas para la creación de objetos del dominio de Pagos"""

from .entidades import Notificacion
from .excepciones import TipoObjetoNoExisteEnDominioNotificacionesExcepcion
from seedwork.dominio.repositorios import Mapeador
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaNotificacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            notificacion: Notificacion = mapeador.dto_a_entidad(obj)

            # Aquí puedes agregar lógica adicional para la creación de la notificación
            return notificacion

@dataclass
class FabricaNotificaciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Notificacion.__class__:
            fabrica_notificacion = _FabricaNotificacion()
            return fabrica_notificacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioNotificacionesExcepcion()