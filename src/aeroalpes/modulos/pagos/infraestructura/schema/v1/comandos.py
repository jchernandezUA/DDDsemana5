# Propósito: Definir el esquema para los comandos que este servicio podría 
# consumir de forma asíncrona.

from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class TransaccionPayload(Record):
    id_referencia = String()
    monto = Float()
    moneda = String()
    descripcion = String()

class ComandoCrearPagoPayload(ComandoIntegracion):
    id_socio = String()
    monto_total = Float()
    moneda = String()
    transacciones = Array(TransaccionPayload())

class ComandoCrearPago(ComandoIntegracion):
    data = ComandoCrearPagoPayload()