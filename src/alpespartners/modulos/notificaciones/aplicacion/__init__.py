from pydispatch import dispatcher
from .handlers import HandlerNotificacionIntegracion, HandlerEventosPago
from ..dominio.eventos import NotificacionCreada, NotificacionEnviada, NotificacionFallida

# Conectar handlers de integración para eventos de notificaciones
dispatcher.connect(HandlerNotificacionIntegracion.handle_notificacion_creada, signal=f'{NotificacionCreada.__name__}Integracion')
dispatcher.connect(HandlerNotificacionIntegracion.handle_notificacion_enviada, signal=f'{NotificacionEnviada.__name__}Integracion')
dispatcher.connect(HandlerNotificacionIntegracion.handle_notificacion_fallida, signal=f'{NotificacionFallida.__name__}Integracion')

# Conectar handlers para eventos de pagos (estos escuchan eventos externos)
# Nota: Los eventos de pagos se manejan vía Pulsar, no pydispatch
print("✅ Módulo de notificaciones cargado - Handlers registrados")
