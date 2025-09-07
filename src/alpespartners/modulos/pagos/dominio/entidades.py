# Propósito: Definir el Agregado Raíz Pago y cualquier otra entidad relevante. 
# Este es el corazón del dominio.


"""Entidades del dominio de Pagos"""

from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import modulos.pagos.dominio.objetos_valor as ov
from modulos.pagos.dominio.eventos import PagoCreado, PagoProcesado, PagoRechazado
from seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Transaccion(Entidad):
    """Entidad que representa una transacción individual de comisión."""
    id_referencia: str = field(hash=True, default=None)
    monto: ov.Monto = field(default_factory=ov.Monto)
    descripcion: str = field(default_factory=str)

@dataclass
class Pago(AgregacionRaiz):
    """Agregado Raíz que representa un pago a un socio."""
    id_socio: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoPago = field(default=ov.EstadoPago.PENDIENTE)
    monto_total: ov.Monto = field(default=None)
    transacciones: list[Transaccion] = field(default_factory=list)

    def crear_pago(self, pago: Pago):
        """
        Método para iniciar la creación del agregado.
        Dispara el evento de dominio inicial.
        """
        self.id_socio = pago.id_socio
        self.estado = pago.estado
        self.monto_total = pago.monto_total
        self.transacciones = pago.transacciones

        self.agregar_evento(PagoCreado(
            pago_id=self.id,
            id_socio=self.id_socio,
            monto_total=self.monto_total.valor,
            moneda=self.monto_total.moneda,
            estado=self.estado.name,
            fecha_creacion=self.fecha_creacion
        ))

    def procesar_pago(self):
        """
        Lógica de negocio para procesar un pago.
        Cambia el estado y dispara un evento.
        """
        if self.estado != ov.EstadoPago.PENDIENTE:
            raise ValueError("Solo se pueden procesar pagos en estado PENDIENTE")
        
        self.estado = ov.EstadoPago.PROCESADO
        self.agregar_evento(PagoProcesado(self.id, self.fecha_actualizacion))

    def rechazar_pago(self, motivo: str):
        """

        Lógica de negocio para rechazar un pago.
        Cambia el estado y dispara un evento con un motivo.
        """
        if self.estado != ov.EstadoPago.PENDIENTE:
            raise ValueError("Solo se pueden rechazar pagos en estado PENDIENTE")

        self.estado = ov.EstadoPago.RECHAZADO
        self.agregar_evento(PagoRechazado(self.id, self.fecha_actualizacion, motivo))