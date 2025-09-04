# Propósito: Manejar los eventos de dominio (PagoCreado, PagoProcesado, etc.) y despacharlos 
# como eventos de integración al message broker a través del Despachador de infraestructura.

from aeroalpes.seedwork.aplicacion.handlers import Handler
from aeroalpes.modulos.pagos.infraestructura.despachadores import Despachador

class HandlerPagoIntegracion(Handler):

    @staticmethod
    def handle_pago_creado(evento):
         # ========== AÑADE ESTA LÍNEA ==========
        print('===================================================================')
        print(f'¡HANDLER: Evento de dominio PagoCreado recibido! ID: {evento.pago_id}')
        print('===================================================================')
        # =======================================
        despachador = Despachador()
        # Publicamos el evento en el tópico 'eventos-pago'
        despachador.publicar_evento(evento, 'eventos-pago')

    @staticmethod
    def handle_pago_procesado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-pago')

    @staticmethod
    def handle_pago_rechazado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-pago')