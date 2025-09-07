# Propósito: Convertir entre las entidades del dominio y los DTOs de aplicación.

from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.notificaciones.dominio.entidades import Notificacion
from modulos.notificaciones.aplicacion.dto import NotificacionDTO, ContenidoDTO
import modulos.notificaciones.dominio.objetos_valor as ov

class MapeadorNotificacion(AppMap):
    
    def obtener_tipo(self) -> type:
        return Notificacion.__class__
    
    def entidad_a_dto(self, entidad: Notificacion) -> NotificacionDTO:
        
        contenido_dto = ContenidoDTO(
            asunto=entidad.contenido.asunto if entidad.contenido else "",
            cuerpo=entidad.contenido.cuerpo if entidad.contenido else ""
        )
        
        fecha_creacion = entidad.fecha_creacion
        fecha_actualizacion = entidad.fecha_actualizacion
        
        return NotificacionDTO(
            id=str(entidad.id),
            destinatario_email=entidad.destinatario_email.valor if entidad.destinatario_email else "",
            tipo_notificacion=entidad.tipo_notificacion.value if entidad.tipo_notificacion else "",
            estado=entidad.estado.value if entidad.estado else "",
            id_pago=str(entidad.id_pago.valor) if entidad.id_pago else "",
            fecha_creacion=fecha_creacion.isoformat() if fecha_creacion else "",
            fecha_actualizacion=fecha_actualizacion.isoformat() if fecha_actualizacion else "",
            contenido=contenido_dto
        )
    
    def dto_a_entidad(self, dto: NotificacionDTO) -> Notificacion:
        notificacion = Notificacion()
        notificacion.destinatario_email = ov.DestinatarioEmail(dto.destinatario_email)
        notificacion.tipo_notificacion = ov.TipoNotificacion(dto.tipo_notificacion)
        notificacion.estado = ov.EstadoNotificacion(dto.estado)
        notificacion.contenido = ov.ContenidoNotificacion(
            asunto=dto.contenido.asunto,
            cuerpo=dto.contenido.cuerpo
        )
        if dto.id_pago:
            notificacion.id_pago = ov.IdPago(dto.id_pago)
        
        return notificacion
