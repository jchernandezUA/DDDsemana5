"""
Fábricas del dominio de Eventos
"""
from dataclasses import dataclass

from modulos.eventos.dominio.excepciones import TipoObjetoNoExisteEnDominioEventosExcepcion
from modulos.eventos.dominio.reglas import MontoDebeSerPositivo
from seedwork.dominio.entidades import Entidad
from seedwork.dominio.repositorios import Mapeador
from .entidades import Evento
from seedwork.dominio.fabricas import Fabrica

@dataclass
class _FabricaEvento(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            evento: Evento = mapeador.dto_a_entidad(obj)

            # Validación de reglas de negocio
            self.validar_regla(MontoDebeSerPositivo(evento.monto))

            return evento

@dataclass
class FabricaEventos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Evento.__class__:
            fabrica_evento = _FabricaEvento()
            return fabrica_evento.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioEventosExcepcion()