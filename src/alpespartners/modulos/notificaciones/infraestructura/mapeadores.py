# Propósito: Convertir entre entidades del dominio y DTOs de infraestructura (SQLAlchemy).

from seedwork.dominio.repositorios import Mapeador
from modulos.notificaciones.dominio.entidades import Notificacion
from modulos.notificaciones.infraestructura.dto import Notificacion as NotificacionDTO
import modulos.notificaciones.dominio.objetos_valor as ov
from datetime import datetime
import uuid

class MapeadorNotificacion(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Notificacion.__class__

    def entidad_a_dto(self, entidad: Notificacion) -> NotificacionDTO:
        
        fecha_creacion = entidad.fecha_creacion
        fecha_actualizacion = entidad.fecha_actualizacion
        
        return NotificacionDTO(
            id=str(entidad.id),
            destinatario_email=entidad.destinatario_email.valor if entidad.destinatario_email else "",
            tipo_notificacion=entidad.tipo_notificacion.value if entidad.tipo_notificacion else "",
            asunto=entidad.contenido.asunto if entidad.contenido else "",
            cuerpo=entidad.contenido.cuerpo if entidad.contenido else "",
            estado=entidad.estado.value if entidad.estado else "",
            id_pago=str(entidad.id_pago.valor) if entidad.id_pago else "",
            fecha_creacion=fecha_creacion,
            fecha_actualizacion=fecha_actualizacion
        )

    def dto_a_entidad(self, dto: NotificacionDTO) -> Notificacion:
        notificacion = Notificacion()
        notificacion.id = uuid.UUID(dto.id)
        notificacion.destinatario_email = ov.DestinatarioEmail(dto.destinatario_email)
        notificacion.tipo_notificacion = ov.TipoNotificacion(dto.tipo_notificacion)
        notificacion.estado = ov.EstadoNotificacion(dto.estado)
        notificacion.contenido = ov.ContenidoNotificacion(
            asunto=dto.asunto,
            cuerpo=dto.cuerpo
        )
        if dto.id_pago:
            notificacion.id_pago = ov.IdPago(uuid.UUID(dto.id_pago))
        notificacion.fecha_creacion = dto.fecha_creacion
        notificacion.fecha_actualizacion = dto.fecha_actualizacion
        
        return notificacion
