# src/aeroalpes/api/pagos.py

import seedwork.presentacion.api as api
import json
from flask import request, Response
from seedwork.dominio.excepciones import ExcepcionDominio

# Importaciones específicas del módulo de Pagos
from modulos.pagos.aplicacion.mapeadores import MapeadorPagoDTOJson
from modulos.pagos.aplicacion.comandos.crear_pago import CrearPago
from modulos.pagos.aplicacion.queries.obtener_pago import ObtenerPago
from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.aplicacion.queries import ejecutar_query

# Creación del Blueprint. La URL base para todas las rutas en este archivo será '/pagos'
bp = api.crear_blueprint('pagos', '/pagos')

# Endpoint para crear un pago. Responde a 'POST /pagos/'
@bp.route('/', methods=('POST',))
def crear_pago_asincrono():
    try:
        pago_dict = request.json
        map_pago = MapeadorPagoDTOJson()
        pago_dto = map_pago.externo_a_dto(pago_dict)

        comando = CrearPago(
            id=pago_dto.id,
            id_socio=pago_dto.id_socio,
            monto_total=pago_dto.monto_total,
            moneda=pago_dto.moneda,
            comisiones=pago_dto.comisiones,
            fecha_creacion=pago_dto.fecha_creacion,
            fecha_actualizacion=pago_dto.fecha_actualizacion
        )
        
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

# Endpoint para obtener un pago. Responde a 'GET /pagos/<id>'
@bp.route('/<id>', methods=('GET',))
def dar_pago_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPago(id))
        map_pago = MapeadorPagoDTOJson()
        
        return map_pago.dto_a_externo(query_resultado.resultado)
    else:
        # Esto podría devolver una lista de todos los pagos o un error
        return Response(json.dumps(dict(error="Se requiere un ID de pago")), status=400, mimetype='application/json')
