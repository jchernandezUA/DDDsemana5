"""
Objetos de Valor del dominio de Eventos
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from typing import Dict, Any, Optional


class TipoEvento(Enum):
    """Enumeración de tipos de eventos soportados"""
    PAGO_CREADO = "pago_creado"
    PAGO_PROCESADO = "pago_procesado"
    PAGO_FALLIDO = "pago_fallido"
    NOTIFICACION_ENVIADA = "notificacion_enviada"
    USUARIO_REGISTRADO = "usuario_registrado"
    RESERVA_CREADA = "reserva_creada"
    RESERVA_CANCELADA = "reserva_cancelada"
    INTEGRACION_EXTERNA = "integracion_externa"
    SISTEMA_INTERNO = "sistema_interno"

    @property
    def valor(self) -> str:
        return self.value
