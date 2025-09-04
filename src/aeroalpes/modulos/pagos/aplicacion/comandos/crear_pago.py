# Propósito: Define el comando CrearPago y su handler, que orquesta la 
# creación de un nuevo pago.

from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.pagos.aplicacion.dto import PagoDTO, ComisionDTO
from .base import PagoBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.pagos.dominio.entidades import Pago
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.pagos.aplicacion.mapeadores import MapeadorPago
from aeroalpes.modulos.pagos.infraestructura.repositorios import RepositorioPagos

@dataclass
class CrearPago(Comando):
    id_socio: str
    monto_total: float
    moneda: str
    comisiones: list[ComisionDTO] = field(default_factory=list)
    # Heredamos los campos base del DTO que necesitemos para la creación
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)


class CrearPagoHandler(PagoBaseHandler):
    
    def handle(self, comando: CrearPago):
        pago_dto = PagoDTO(
            id=comando.id,
            id_socio=comando.id_socio,
            monto_total=comando.monto_total,
            moneda=comando.moneda,
            comisiones=comando.comisiones,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion
        )

        pago: Pago = self.fabrica_pagos.crear_objeto(pago_dto, MapeadorPago())
        pago.crear_pago(pago) # Método del agregado que dispara el evento de dominio

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPagos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, pago)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPago)
def ejecutar_comando_crear_pago(comando: CrearPago):
    handler = CrearPagoHandler()
    handler.handle(comando)