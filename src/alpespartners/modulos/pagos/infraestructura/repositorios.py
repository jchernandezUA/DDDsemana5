# Propósito: Implementación concreta del RepositorioPagos usando SQLAlchemy.

from config.db import db
from modulos.pagos.dominio.repositorios import RepositorioPagos
from modulos.pagos.dominio.entidades import Pago
from modulos.pagos.dominio.fabricas import FabricaPagos
from .dto import Pago as PagoDTO
from .mapeadores import MapeadorPago
from uuid import UUID

class RepositorioPagosSQLite(RepositorioPagos):
    def __init__(self):
        self._fabrica_pagos: FabricaPagos = FabricaPagos()

    @property
    def fabrica_pagos(self):
        return self._fabrica_pagos

    def obtener_por_id(self, id: UUID) -> Pago:
        pago_dto = db.session.query(PagoDTO).filter_by(id=str(id)).one()
        return self.fabrica_pagos.crear_objeto(pago_dto, MapeadorPago())

    def obtener_todos(self) -> list[Pago]:
        # Implementar lógica para obtener todos si es necesario
        raise NotImplementedError

    def agregar(self, pago: Pago):
        pago_dto = self.fabrica_pagos.crear_objeto(pago, MapeadorPago())
        db.session.add(pago_dto)

    def actualizar(self, pago: Pago):
        pago_dto = self.fabrica_pagos.crear_objeto(pago, MapeadorPago())
        db.session.merge(pago_dto) # Merge para actualizar

    def eliminar(self, pago_id: UUID):
        # Implementar lógica de eliminación si es necesario
        raise NotImplementedError
