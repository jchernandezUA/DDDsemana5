# Propósito: Definir los modelos de persistencia (SQLAlchemy) que representan las tablas 
# en la base de datos para el módulo de pagos.



"""DTOs (modelos de persistencia) para la capa de infraestructura del dominio de Pagos"""

from config.db import db
import uuid

# Tabla intermedia para la relación muchos-a-muchos entre Pagos y Transacciones
pagos_transacciones = db.Table(
    "pagos_transacciones",
    db.Model.metadata,
    db.Column("pago_id", db.String, db.ForeignKey("pagos.id")),
    db.Column("transaccion_id", db.String, db.ForeignKey("transacciones.id")),
)

class Transaccion(db.Model):
    __tablename__ = "transacciones"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_referencia = db.Column(db.String, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    moneda = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=True)

class Pago(db.Model):
    __tablename__ = "pagos"
    id = db.Column(db.String, primary_key=True)
    id_socio = db.Column(db.String, nullable=False)
    monto_total = db.Column(db.Float, nullable=False)
    moneda = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    transacciones = db.relationship('Transaccion', secondary=pagos_transacciones, backref='pagos')