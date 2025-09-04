# src/aeroalpes/modulos/pagos/infraestructura/excepciones.py
from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado en el módulo de pagos.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)