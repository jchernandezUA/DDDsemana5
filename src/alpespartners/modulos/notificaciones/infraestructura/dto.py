# Propósito: Definir los modelos de persistencia (SQLAlchemy) que representan las tablas 
# en la base de datos para el módulo de notificaciones.

"""DTOs (modelos de persistencia) para la capa de infraestructura del dominio de Notificaciones"""

from config.db import db
import uuid

class Notificacion(db.Model):
    __tablename__ = "notificaciones"
    
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    destinatario_email = db.Column(db.String(255), nullable=False)
    tipo_notificacion = db.Column(db.String(50), nullable=False)
    asunto = db.Column(db.String(500), nullable=False)
    cuerpo = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(50), nullable=False, default="Pendiente")
    id_pago = db.Column(db.String, nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
