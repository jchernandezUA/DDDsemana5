# Propósito: Definir el Agregado Raíz Notificacion y cualquier otra entidad relevante.
# Este es el corazón del dominio.

"""Entidades del dominio de Notificaciones"""

from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import modulos.notificaciones.dominio.objetos_valor as ov
from modulos.notificaciones.dominio.eventos import NotificacionCreada, NotificacionEnviada, NotificacionFallida
from seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Notificacion(AgregacionRaiz):
    """Agregado Raíz que representa una notificación."""
    destinatario_email: ov.DestinatarioEmail = field(default=None)
    tipo_notificacion: ov.TipoNotificacion = field(default=None)
    contenido: ov.ContenidoNotificacion = field(default=None)
    estado: ov.EstadoNotificacion = field(default=ov.EstadoNotificacion.PENDIENTE)
    id_pago: ov.IdPago = field(default=None)

    def crear_notificacion(self, notificacion: Notificacion):
        """
        Método para iniciar la creación del agregado.
        Dispara el evento de dominio inicial.
        """
        self.destinatario_email = notificacion.destinatario_email
        self.tipo_notificacion = notificacion.tipo_notificacion
        self.contenido = notificacion.contenido
        self.estado = notificacion.estado
        self.id_pago = notificacion.id_pago

        self.agregar_evento(NotificacionCreada(
            notificacion_id=self.id,
            destinatario_email=self.destinatario_email.valor,
            tipo_notificacion=self.tipo_notificacion.value,
            asunto=self.contenido.asunto,
            cuerpo=self.contenido.cuerpo,
            id_pago=self.id_pago.valor if self.id_pago else None,
            fecha_creacion=self.fecha_creacion
        ))

    def marcar_como_enviada(self):
        """
        Marca la notificación como enviada exitosamente.
        """
        if self.estado == ov.EstadoNotificacion.PENDIENTE:
            self.estado = ov.EstadoNotificacion.ENVIADA
            self.agregar_evento(NotificacionEnviada(
                notificacion_id=self.id,
                destinatario_email=self.destinatario_email.valor,
                fecha_envio=self.fecha_actualizacion
            ))

    def marcar_como_fallida(self, motivo: str):
        """
        Marca la notificación como fallida.
        """
        if self.estado == ov.EstadoNotificacion.PENDIENTE:
            self.estado = ov.EstadoNotificacion.FALLIDA
            self.agregar_evento(NotificacionFallida(
                notificacion_id=self.id,
                destinatario_email=self.destinatario_email.valor,
                motivo_falla=motivo,
                fecha_falla=self.fecha_actualizacion
            ))
