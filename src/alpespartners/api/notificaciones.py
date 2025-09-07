# src/aeroalpes/api/notificaciones.py

import seedwork.presentacion.api as api
import json
from flask import request, Response, jsonify
from seedwork.dominio.excepciones import ExcepcionDominio

# Creación del Blueprint. La URL base para todas las rutas en este archivo será '/notificaciones'
bp = api.crear_blueprint('notificaciones', '/notificaciones')

# Endpoint de health check. Responde a 'GET /notificaciones/health'
@bp.route('/health', methods=('GET',))
def health_check():
    return jsonify({
        'status': 'OK',
        'servicio': 'notificaciones',
        'version': '1.0',
        'mensaje': 'Servicio de notificaciones funcionando correctamente'
    })

# Endpoint para probar funcionalidad. Responde a 'GET /notificaciones/test'
@bp.route('/test', methods=('GET',))
def test_notificaciones():
    return jsonify({
        'test': 'OK',
        'servicio': 'notificaciones',
        'endpoints_disponibles': [
            'GET /notificaciones/health',
            'GET /notificaciones/test',
            'GET /notificaciones/stats'
        ]
    })

# Endpoint para estadísticas básicas. Responde a 'GET /notificaciones/stats'
@bp.route('/stats', methods=('GET',))
def obtener_estadisticas():
    try:
        # Por ahora retornamos estadísticas de ejemplo
        # Más adelante se conectará con la base de datos
        return jsonify({
            'total_notificaciones': 0,
            'enviadas': 0,
            'pendientes': 0,
            'fallidas': 0,
            'porcentaje_exito': 0,
            'mensaje': 'Estadísticas de ejemplo - conexión con BD pendiente'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'mensaje': 'Error obteniendo estadísticas'
        })
