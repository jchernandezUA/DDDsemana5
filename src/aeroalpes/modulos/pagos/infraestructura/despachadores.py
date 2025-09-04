import pulsar
from pulsar.schema import *
import datetime

# Importamos TODOS los eventos y payloads que este despachador puede manejar
from aeroalpes.modulos.pagos.infraestructura.schema.v1.eventos import (
    EventoPagoCreado, PagoCreadoPayload,
    EventoPagoProcesado, PagoProcesadoPayload,
    EventoPagoRechazado, PagoRechazadoPayload
)
# Importamos los eventos de DOMINIO para poder identificarlos
from aeroalpes.modulos.pagos.dominio.eventos import PagoCreado, PagoProcesado, PagoRechazado

from aeroalpes.seedwork.infraestructura import utils

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # Obtenemos el schema del propio objeto del mensaje
        publicador = cliente.create_producer(topico, schema=AvroSchema(mensaje.__class__))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # ========== AÑADE ESTA LÍNEA ==========
        print('===================================================================')
        print(f'¡DESPACHADOR: Publicando evento en el tópico {topico}! ID: {evento.pago_id}')
        print('===================================================================')
        # =======================================
        # Determinamos el tipo de evento de dominio para saber qué payload crear
        if isinstance(evento, PagoCreado):
            payload = PagoCreadoPayload(
                id_pago=str(evento.pago_id), 
                id_socio=str(evento.id_socio), 
                monto_total=float(evento.monto_total),
                moneda=str(evento.moneda),
                estado=str(evento.estado), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoPagoCreado(data=payload)
        elif isinstance(evento, PagoProcesado):
            payload = PagoProcesadoPayload(
                id_pago=str(evento.pago_id),
                fecha_actualizacion=int(unix_time_millis(evento.fecha_actualizacion))
            )
            evento_integracion = EventoPagoProcesado(data=payload)
        elif isinstance(evento, PagoRechazado):
            payload = PagoRechazadoPayload(
                id_pago=str(evento.pago_id),
                motivo=str(evento.motivo),
                fecha_actualizacion=int(unix_time_millis(evento.fecha_actualizacion))
            )
            evento_integracion = EventoPagoRechazado(data=payload)
        else:
            # Si no reconocemos el evento, no hacemos nada.
            # Podríamos también lanzar un error.
            return

        # Publicamos el evento de integración que acabamos de crear
        self._publicar_mensaje(evento_integracion, topico)