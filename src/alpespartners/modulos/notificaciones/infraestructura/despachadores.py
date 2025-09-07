# Propósito: Despachar eventos de notificaciones al message broker (Pulsar).

import pulsar
from pulsar.schema import *
import logging
import traceback

from seedwork.infraestructura import utils
from modulos.notificaciones.infraestructura.schema.v1.eventos import EventoNotificacionCreada, EventoNotificacionEnviada, EventoNotificacionFallida

class Despachador:
    
    def __init__(self):
        self._cliente = None
        self._publicador = None

    def _obtener_publicador(self, topico):
        """Crea un publicador para el tópico específico."""
        if self._cliente is None:
            self._cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        
        # Determinar el schema basado en el tópico
        schema = AvroSchema(EventoNotificacionCreada)  # Schema por defecto
        
        return self._cliente.create_producer(topico, schema=schema)

    def publicar_evento(self, evento, topico):
        """Publica un evento de notificación en el tópico especificado."""
        try:
            publicador = self._obtener_publicador(topico)
            
            # Mapear el evento de dominio al evento de infraestructura
            if evento.__class__.__name__ == 'NotificacionCreada':
                evento_schema = EventoNotificacionCreada(
                    notificacion_id=str(evento.notificacion_id),
                    destinatario_email=evento.destinatario_email,
                    tipo_notificacion=evento.tipo_notificacion,
                    asunto=evento.asunto,
                    cuerpo=evento.cuerpo,
                    id_pago=str(evento.id_pago) if evento.id_pago else "",
                    fecha_creacion=evento.fecha_creacion.isoformat() if evento.fecha_creacion else ""
                )
            elif evento.__class__.__name__ == 'NotificacionEnviada':
                evento_schema = EventoNotificacionEnviada(
                    notificacion_id=str(evento.notificacion_id),
                    destinatario_email=evento.destinatario_email,
                    fecha_envio=evento.fecha_envio.isoformat() if evento.fecha_envio else ""
                )
            elif evento.__class__.__name__ == 'NotificacionFallida':
                evento_schema = EventoNotificacionFallida(
                    notificacion_id=str(evento.notificacion_id),
                    destinatario_email=evento.destinatario_email,
                    motivo_falla=evento.motivo_falla,
                    fecha_falla=evento.fecha_falla.isoformat() if evento.fecha_falla else ""
                )
            else:
                logging.warning(f"Tipo de evento no reconocido: {evento.__class__.__name__}")
                return

            publicador.send(evento_schema)
            logging.info(f'Evento {evento.__class__.__name__} publicado en tópico {topico}')
            
        except Exception as e:
            logging.error(f'Error publicando evento en tópico {topico}: {str(e)}')
            traceback.print_exc()
        finally:
            if publicador:
                publicador.close()

    def cerrar_conexion(self):
        """Cierra la conexión con Pulsar."""
        if self._cliente:
            self._cliente.close()
