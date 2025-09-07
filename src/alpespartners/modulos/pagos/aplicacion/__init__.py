from pydispatch import dispatcher
from .handlers import HandlerPagoIntegracion
from ..dominio.eventos import PagoCreado, PagoProcesado, PagoRechazado

# --- ¡ESTA ES LA CORRECCIÓN CLAVE! ---
# La Unit of Work emite la señal con el sufijo 'Integracion' DESPUÉS del commit.
# El handler de integración debe escuchar esta señal específica.

dispatcher.connect(HandlerPagoIntegracion.handle_pago_creado, signal=f'{PagoCreado.__name__}Integracion')
dispatcher.connect(HandlerPagoIntegracion.handle_pago_procesado, signal=f'{PagoProcesado.__name__}Integracion')
dispatcher.connect(HandlerPagoIntegracion.handle_pago_rechazado, signal=f'{PagoRechazado.__name__}Integracion')