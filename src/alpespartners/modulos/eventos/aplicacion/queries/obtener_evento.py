# Propósito: Define la consulta ObtenerPago y su handler para recuperar un pago por su ID.

from alpespartners.modulos.eventos.dominio.repositorios import RepositorioEventos
from alpespartners.modulos.eventos.infraestructura.mapeadores import MapeadorEvento
from seedwork.aplicacion.queries import Query, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from dataclasses import dataclass
from .base import EventoQueryBaseHandler

@dataclass
class ObtenerEvento(Query):
    id: str

class ObtenerEventoHandler(EventoQueryBaseHandler):

    def handle(self, query: ObtenerEvento) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEventos.__class__)
        evento =  self.fabrica_eventos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorEvento())
        return QueryResultado(resultado=evento)

@query.register(ObtenerEvento)
def ejecutar_query_obtener_evento(query: ObtenerEvento):
    handler = ObtenerEventoHandler()
    return handler.handle(query)