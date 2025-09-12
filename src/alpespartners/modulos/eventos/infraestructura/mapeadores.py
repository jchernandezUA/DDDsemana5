"""
Mapeadores para el módulo de Eventos
"""
from datetime import datetime
from modulos.eventos.dominio.objetos_valor import TipoEvento
from modulos.eventos.dominio.entidades import Evento
from seedwork.dominio.repositorios import Mapeador
from .dto import EventoEntity as EventoDTO

class MapeadorEvento(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def obtener_tipo(self) -> type:
        return Evento.__class__

    def entidad_a_dto(self, entidad: Evento) -> EventoDTO:
        print(f"DEBUG - Entidad fecha: {entidad.fecha_creacion}")  # Debug
        print(f"DEBUG - Entidad tipo: {entidad.tipo}")  # Debug
        print(f"DEBUG - Entidad tipo valor: {entidad.tipo.value}")  # Debug
        evento_dto = EventoDTO()
        evento_dto.id = str(entidad.id)
        evento_dto.tipo = str(entidad.tipo.value)
        evento_dto.id_socio = str(entidad.id_socio)
        evento_dto.id_programa = str(entidad.id_programa)
        evento_dto.monto = entidad.monto
        evento_dto.fecha_creacion = entidad.fecha_creacion
        evento_dto.fecha_procesamiento = entidad.fecha_procesamiento

        return evento_dto

    def dto_a_entidad(self, dto: EventoDTO) -> Evento:
        fecha_creacion = None
        if dto.fecha_creacion:
            if isinstance(dto.fecha_creacion, str):
                fecha_creacion = datetime.strptime(dto.fecha_creacion, self._FORMATO_FECHA)
            else:
                fecha_creacion = dto.fecha_creacion
        
        fecha_procesamiento = None
        if dto.fecha_procesamiento:
            if isinstance(dto.fecha_procesamiento, str):
                fecha_procesamiento = datetime.strptime(dto.fecha_procesamiento, self._FORMATO_FECHA)
            else:
                fecha_procesamiento = dto.fecha_procesamiento
        evento = Evento(
            id=dto.id,
            tipo=TipoEvento(dto.tipo),
            id_socio=dto.id_socio,
            id_programa=dto.id_programa,
            monto=dto.monto,
            fecha_creacion=fecha_creacion,
            fecha_procesamiento=fecha_procesamiento
        )

        return evento