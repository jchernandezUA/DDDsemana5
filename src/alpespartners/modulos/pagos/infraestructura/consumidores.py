import pulsar, _pulsar  
import logging
import traceback
from pulsar.schema import *

# Importamos los schemas específicos de PAGOS
from modulos.pagos.infraestructura.schema.v1.eventos import EventoPagoCreado
from modulos.pagos.infraestructura.schema.v1.comandos import ComandoCrearPago
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'eventos-pago', # <--- TÓPICO DE EVENTOS DE PAGO
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='aeroalpes-sub-eventos-pagos', # Nombre único de suscripción
            schema=AvroSchema(EventoPagoCreado) # Schema de eventos de pago
        )

        while True:
            mensaje = consumidor.receive()
            # Opcional: imprimir para ver que el servicio principal recibe eventos
            print(f'Evento de PAGO recibido en servicio principal: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de PAGO!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'comandos-pago', # <--- TÓPICO DE COMANDOS DE PAGO
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='aeroalpes-sub-comandos-pagos', # Nombre único
            schema=AvroSchema(ComandoCrearPago) # Schema de comandos de pago
        )

        while True:
            mensaje = consumidor.receive()
            # Opcional: imprimir para ver que el servicio principal recibe comandos
            print(f'Comando de PAGO recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de comandos de PAGO!')
        traceback.print_exc()
        if cliente:
            cliente.close()