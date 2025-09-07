import pulsar, _pulsar  
import logging
import traceback
from pulsar.schema import *

# Importamos los schemas específicos de NOTIFICACIONES
from modulos.notificaciones.infraestructura.schema.v1.eventos import EventoNotificacionCreada
from modulos.pagos.infraestructura.schema.v1.eventos import EventoPagoCreado
from modulos.notificaciones.aplicacion.handlers import HandlerEventosPago
from seedwork.infraestructura import utils

def suscribirse_a_eventos_notificaciones():
    """Suscribirse a eventos propios del módulo de notificaciones."""
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'eventos-notificacion', # <--- TÓPICO DE EVENTOS DE NOTIFICACIONES
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='aeroalpes-sub-eventos-notificaciones', # Nombre único de suscripción
            schema=AvroSchema(EventoNotificacionCreada) # Schema de eventos de notificaciones
        )

        while True:
            mensaje = consumidor.receive()
            # Opcional: imprimir para ver que el servicio principal recibe eventos
            print(f'Evento de NOTIFICACIÓN recibido en servicio principal: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de NOTIFICACIONES!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_pagos():
    """Suscribirse a eventos de pagos para crear notificaciones automáticamente."""
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'eventos-pago', # <--- TÓPICO DE EVENTOS DE PAGOS
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='notificaciones-sub-eventos-pagos', # Nombre único de suscripción
            schema=AvroSchema(EventoPagoCreado) # Schema de eventos de pagos
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Evento de PAGO recibido en módulo de notificaciones: {mensaje.value().data}')
            
            # Procesar el evento según su tipo
            evento_data = mensaje.value().data
            
            # Simular el procesamiento basado en el tipo de evento
            # En una implementación real, aquí se analizaría el tipo de evento
            if hasattr(evento_data, 'id_pago'):
                # Crear un objeto evento simple para el handler
                class EventoPago:
                    def __init__(self, data):
                        self.id_pago = data.id_pago
                        self.monto_total = getattr(data, 'monto_total', 0)
                        self.moneda = getattr(data, 'moneda', 'COP')
                        self.estado = getattr(data, 'estado', 'CREADO')
                
                evento = EventoPago(evento_data)
                
                # Llamar al handler apropiado según el estado
                if evento.estado == 'CREADO' or evento.estado == 'PENDIENTE':
                    HandlerEventosPago.handle_pago_creado(evento)
                elif evento.estado == 'PROCESADO' or evento.estado == 'Procesado':
                    HandlerEventosPago.handle_pago_procesado(evento)
                elif evento.estado == 'RECHAZADO' or evento.estado == 'Rechazado':
                    HandlerEventosPago.handle_pago_rechazado(evento)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de PAGOS desde notificaciones!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def iniciar_consumidores_notificaciones():
    """Inicia todos los consumidores del módulo de notificaciones."""
    print("Iniciando consumidores del módulo de notificaciones...")
    
    # Ejecutar ambos consumidores (en una implementación real, estos irían en hilos separados)
    try:
        # Suscribirse a eventos de pagos para crear notificaciones
        suscribirse_a_eventos_pagos()
    except Exception as e:
        logging.error(f"Error iniciando consumidores de notificaciones: {str(e)}")
        traceback.print_exc()
