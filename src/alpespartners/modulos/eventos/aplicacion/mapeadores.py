from datetime import datetime
import uuid
from modulos.eventos.dominio.entidades import Evento
from modulos.eventos.dominio.objetos_valor import TipoEvento
from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap

# Importamos los DTOs de la capa de aplicación
from .dto import EventoDTO


class MapeadorEventoDTOJson(AppMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def externo_a_dto(self, externo: dict) -> EventoDTO:
        fecha_actual = datetime.now().strftime(self._FORMATO_FECHA)
        evento_dto = EventoDTO(
            tipo=externo.get('tipoEvento'),
            id_socio=externo.get('idSocio'),
            id_referido=externo.get('idReferido'),
            monto=externo.get('monto'),
            fecha_evento=externo.get('fechaEvento', fecha_actual)
        )
        return evento_dto

    def dto_a_externo(self, dto: EventoDTO) -> dict:
        return dto.__dict__

class MapeadorEvento(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Evento.__class__

    def entidad_a_dto(self, entidad: Evento) -> EventoDTO:
        _id = str(entidad.id)
        _id_socio = str(entidad.id_socio)
        _id_programa = str(entidad.id_programa)
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_procesamiento = entidad.fecha_procesamiento.strftime(self._FORMATO_FECHA) if entidad.fecha_procesamiento else None

        return EventoDTO(
            id=_id,
            tipo=entidad.tipo.valor,
            id_socio=_id_socio,
            id_programa=_id_programa,
            monto=entidad.monto,
            fecha_creacion=fecha_creacion,
            fecha_procesamiento=fecha_procesamiento
        )

    def dto_a_entidad(self, dto: EventoDTO) -> Evento:
        evento = Evento()
        evento.id_socio = uuid.UUID(dto.id_socio)
        evento.id_programa = uuid.UUID(dto.id_programa)
        evento.tipo = TipoEvento(dto.tipo)
        evento.monto = dto.monto
        evento.fecha_creacion = datetime.strptime(dto.fecha_creacion, self._FORMATO_FECHA)
        evento.fecha_procesamiento = datetime.strptime(dto.fecha_procesamiento, self._FORMATO_FECHA)

        return evento