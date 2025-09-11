# Propósito: Define el comando CrearPago y su handler, que orquesta la 
# creación de un nuevo pago.

from alpespartners.modulos.eventos.aplicacion.dto import EventoDTO
from alpespartners.modulos.eventos.dominio.entidades import Evento
from alpespartners.modulos.eventos.dominio.repositorios import RepositorioEventos
from alpespartners.modulos.eventos.infraestructura.mapeadores import MapeadorEvento
from seedwork.aplicacion.comandos import Comando
from .base import EventoBaseHandler
from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import ejecutar_commando as comando

from seedwork.infraestructura.uow import UnidadTrabajoPuerto

@dataclass
class CrearEvento(Comando):
    id: str
    tipo: str
    id_socio: str
    id_programa: str
    monto: float


class CrearEventoHandler(EventoBaseHandler):

    def handle(self, comando: CrearEvento):
        evento_dto = EventoDTO(
            id=comando.id,
            tipo=comando.tipo,
            id_socio=comando.id_socio,
            id_programa=comando.id_programa,
            monto=comando.monto
        )

        evento: Evento = self.fabrica_eventos.crear_objeto(evento_dto, MapeadorEvento())
        evento.crear_evento(evento) # Método del agregado que dispara el evento de dominio

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioEventos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, evento)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearEvento)
def ejecutar_comando_crear_evento(comando: CrearEvento):
    handler = CrearEventoHandler()
    handler.handle(comando)