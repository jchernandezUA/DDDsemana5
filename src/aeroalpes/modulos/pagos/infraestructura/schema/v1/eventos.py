# Propósito: Definir el contrato público (esquema Avro/Pulsar) 
# para los eventos de integración que el servicio de pagos publicará.

from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PagoCreadoPayload(Record):
    id_pago = String()
    id_socio = String()
    monto_total = Float()
    moneda = String()
    estado = String()
    fecha_creacion = Long()

class EventoPagoCreado(EventoIntegracion):
    data = PagoCreadoPayload()

class PagoProcesadoPayload(Record):
    id_pago = String()
    fecha_actualizacion = Long()

class EventoPagoProcesado(EventoIntegracion):
    data = PagoProcesadoPayload()

class PagoRechazadoPayload(Record):
    id_pago = String()
    motivo = String()
    fecha_actualizacion = Long()

class EventoPagoRechazado(EventoIntegracion):
    data = PagoRechazadoPayload()