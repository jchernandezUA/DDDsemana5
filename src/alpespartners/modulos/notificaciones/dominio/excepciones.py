"""Excepciones del dominio de Notificaciones"""

from seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioNotificacionesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de notificaciones'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)