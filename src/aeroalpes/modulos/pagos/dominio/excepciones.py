# Propósito: Definir excepciones personalizadas para el dominio de pagos, 
# lo que mejora la claridad del código.



"""Excepciones del dominio de Pagos"""

from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPagosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de pagos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)