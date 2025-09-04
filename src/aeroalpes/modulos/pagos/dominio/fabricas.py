# Propósito: Crear el agregado Pago de forma segura, aplicando las reglas de negocio definidas.

"""Fábricas para la creación de objetos del dominio de Pagos"""

from .entidades import Pago
from .reglas import MontoDebeSerPositivo, PagoDebeContenerTransacciones
from .excepciones import TipoObjetoNoExisteEnDominioPagosExcepcion
from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPago(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            pago: Pago = mapeador.dto_a_entidad(obj)

            # Validación de reglas de negocio
            self.validar_regla(MontoDebeSerPositivo(pago.monto_total))
            self.validar_regla(PagoDebeContenerTransacciones(pago.transacciones))
            
            return pago

@dataclass
class FabricaPagos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Pago.__class__:
            fabrica_pago = _FabricaPago()
            return fabrica_pago.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPagosExcepcion()