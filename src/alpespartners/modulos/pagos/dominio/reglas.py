# Propósito: Definir reglas de negocio de forma explícita, 
# haciéndolas reutilizables y fáciles de validar.

"""Reglas de negocio del dominio de Pagos"""

from seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Monto
from .entidades import Transaccion

class MontoDebeSerPositivo(ReglaNegocio):
    monto: Monto

    def __init__(self, monto: Monto, mensaje='El monto total del pago debe ser un valor positivo'):
        super().__init__(mensaje)
        self.monto = monto

    def es_valido(self) -> bool:
        return self.monto and self.monto.es_positivo()

class PagoDebeContenerTransacciones(ReglaNegocio):
    transacciones: list[Transaccion]

    def __init__(self, transacciones: list[Transaccion], mensaje='Un pago debe contener al menos una transacción'):
        super().__init__(mensaje)
        self.transacciones = transacciones

    def es_valido(self) -> bool:
        return self.transacciones and len(self.transacciones) > 0