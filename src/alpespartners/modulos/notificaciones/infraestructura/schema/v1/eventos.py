# Propósito: Definir los schemas de Pulsar para los eventos de notificaciones.

from pulsar.schema import Record, String

class EventoNotificacionCreada(Record):
    notificacion_id = String()
    destinatario_email = String()
    tipo_notificacion = String()
    asunto = String()
    cuerpo = String()
    id_pago = String()
    fecha_creacion = String()

class EventoNotificacionEnviada(Record):
    notificacion_id = String()
    destinatario_email = String()
    fecha_envio = String()

class EventoNotificacionFallida(Record):
    notificacion_id = String()
    destinatario_email = String()
    motivo_falla = String()
    fecha_falla = String()
