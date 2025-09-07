# Propósito: Manejar los eventos de dominio de notificaciones y eventos de pagos para
# crear y procesar notificaciones automáticamente.

import logging
from seedwork.aplicacion.handlers import Handler
from modulos.notificaciones.infraestructura.despachadores import Despachador
from modulos.notificaciones.dominio.entidades import Notificacion
from modulos.notificaciones.infraestructura.servicio_email import ServicioEmail
from modulos.notificaciones.infraestructura.repositorios import RepositorioNotificacionesSQLAlchemy
from config.db import db
import modulos.notificaciones.dominio.objetos_valor as ov

class HandlerNotificacionIntegracion(Handler):

    @staticmethod
    def handle_notificacion_creada(evento):
        print('===================================================================')
        print(f'¡HANDLER: Evento NotificacionCreada recibido! ID: {evento.notificacion_id}')
        print('===================================================================')
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-notificacion')

    @staticmethod
    def handle_notificacion_enviada(evento):
        print('===================================================================')
        print(f'¡HANDLER: Evento NotificacionEnviada recibido! ID: {evento.notificacion_id}')
        print('===================================================================')
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-notificacion')

    @staticmethod
    def handle_notificacion_fallida(evento):
        print('===================================================================')
        print(f'¡HANDLER: Evento NotificacionFallida recibido! ID: {evento.notificacion_id}')
        print('===================================================================')
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-notificacion')

class HandlerEventosPago(Handler):
    """Handler que escucha eventos de pagos y crea notificaciones automáticamente."""

    @staticmethod
    def handle_pago_creado(evento):
        print('===================================================================')
        print(f'¡NOTIFICACIONES: Pago creado detectado! ID: {evento.id_pago}')
        print('===================================================================')
        
        # Crear notificación para pago creado
        notificacion = Notificacion()
        notificacion.destinatario_email = ov.DestinatarioEmail("socio@com")
        notificacion.tipo_notificacion = ov.TipoNotificacion.PAGO_CREADO
        notificacion.contenido = ov.ContenidoNotificacion(
            asunto="Nuevo pago creado",
            cuerpo=f"Se ha creado un nuevo pago con ID: {evento.id_pago} por un monto de {evento.monto_total} {evento.moneda}"
        )
        notificacion.id_pago = ov.IdPago(evento.id_pago)
        
        # Crear la notificación (dispara evento NotificacionCreada)
        notificacion.crear_notificacion(notificacion)
        
        # ========== PERSISTIR EN BASE DE DATOS ==========
        """ repositorio = RepositorioNotificacionesSQLAlchemy()
        try:
            repositorio.agregar(notificacion)
            db.session.commit()
            print(f'✅ Notificación guardada en BD con ID: {notificacion.id}')
        except Exception as e:
            db.session.rollback()
            print(f'❌ Error guardando notificación en BD: {str(e)}') """
            
        print(f'✅ Notificación creada en memoria con ID: {notificacion.id}')
        # ==============================================
        
        # Simular envío de email
        servicio_email = ServicioEmail()
        try:
            servicio_email.enviar_email(
                destinatario=notificacion.destinatario_email.valor,
                asunto=notificacion.contenido.asunto,
                cuerpo=notificacion.contenido.cuerpo
            )
            notificacion.marcar_como_enviada()
            
            # Actualizar estado en BD
            """ try:
                repositorio.actualizar(notificacion)
                db.session.commit()
                print(f'✅ Estado actualizado a ENVIADA en BD')
            except Exception as e:
                db.session.rollback()
                print(f'❌ Error actualizando estado en BD: {str(e)}') """
            print(f'✅ Notificación marcada como ENVIADA en memoria con ID: {notificacion.id}')
                
        except Exception as e:
            notificacion.marcar_como_fallida(str(e))
            
            # Actualizar estado en BD
            """ try:
                repositorio.actualizar(notificacion)
                db.session.commit()
                print(f'✅ Estado actualizado a FALLIDA en BD')
            except Exception as e:
                db.session.rollback()
                print(f'❌ Error actualizando estado en BD: {str(e)}') """
            print(f'✅ Notificación marcada como FALLIDA en memoria con ID: {notificacion.id}')

