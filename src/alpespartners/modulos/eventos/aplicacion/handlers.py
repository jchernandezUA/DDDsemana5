"""
Handlers de aplicación para el módulo de Eventos
"""
from modulos.eventos.infraestructura.despachadores import Despachador
from seedwork.aplicacion.handlers import Handler

class HandlerEventoIntegracion(Handler):

    @staticmethod
    def handle_evento_creado(evento):
        print('===================================================================')
        print(f'¡HANDLER: Evento de dominio EventoCreado recibido! ID: {evento.id}')
        print('===================================================================')
        # =======================================
        despachador = Despachador()
        # Publicamos el evento en el tópico 'eventos'
        despachador.publicar_evento(evento, 'eventos')