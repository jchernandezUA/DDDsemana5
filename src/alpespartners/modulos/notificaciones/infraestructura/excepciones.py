# Propósito: Definir las excepciones específicas de la infraestructura de notificaciones.

from seedwork.dominio.excepciones import ExcepcionFabrica

class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado en el módulo de notificaciones.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class ErrorEnvioEmail(Exception):
    """Se lanza cuando hay un error enviando el email."""
    ...

class ErrorConexionBroker(Exception):
    """Se lanza cuando hay un error conectando con el message broker."""
    ...
