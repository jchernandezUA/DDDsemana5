# Propósito: Define la consulta ObtenerPago y su handler para recuperar un pago por su ID.

from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.pagos.infraestructura.repositorios import RepositorioPagos
from dataclasses import dataclass
from .base import PagoQueryBaseHandler
from modulos.pagos.aplicacion.mapeadores import MapeadorPago
import uuid

@dataclass
class ObtenerPago(Query):
    id: str

class ObtenerPagoHandler(PagoQueryBaseHandler):

    def handle(self, query: ObtenerPago) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPagos.__class__)
        pago =  self.fabrica_pagos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPago())
        return QueryResultado(resultado=pago)

@query.register(ObtenerPago)
def ejecutar_query_obtener_pago(query: ObtenerPago):
    handler = ObtenerPagoHandler()
    return handler.handle(query)