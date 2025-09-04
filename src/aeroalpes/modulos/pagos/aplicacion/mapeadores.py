from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap

# --- IMPORTACIONES CORREGIDAS ---
# Importamos las Entidades 'Pago' y 'Transaccion' desde el dominio
from aeroalpes.modulos.pagos.dominio.entidades import Pago, Transaccion
# Importamos los Objetos Valor
from aeroalpes.modulos.pagos.dominio.objetos_valor import Monto, IdSocio
# Importamos los DTOs de la capa de aplicación
from .dto import PagoDTO, ComisionDTO

from datetime import datetime
import uuid # <-- ¡AÑADIMOS EL IMPORT DE UUID!
# --- FIN DE IMPORTACIONES CORREGIDAS ---


# El resto del archivo (las clases MapeadorPagoDTOJson y MapeadorPago) se mantiene igual
# con la función dto_a_entidad que te proporcioné en la respuesta anterior.

class MapeadorPagoDTOJson(AppMap):
    # ... (sin cambios aquí) ...
    def externo_a_dto(self, externo: dict) -> PagoDTO:
        # Aquí asumimos que 'externo' es un diccionario JSON de una solicitud API
        comisiones_dto = [ComisionDTO(**c) for c in externo.get('comisiones', [])]
        
        pago_dto = PagoDTO(
            id_socio=externo.get('id_socio'),
            monto_total=externo.get('monto_total'),
            moneda=externo.get('moneda'),
            comisiones=comisiones_dto
        )
        return pago_dto

    def dto_a_externo(self, dto: PagoDTO) -> dict:
        return dto.__dict__

class MapeadorPago(RepMap):
    # ... (sin cambios aquí) ...
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pago.__class__

    def entidad_a_dto(self, entidad: Pago) -> PagoDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _id_socio = str(entidad.id_socio.valor)
        
        return PagoDTO(
            id=_id,
            id_socio=_id_socio,
            monto_total=entidad.monto_total.valor,
            moneda=entidad.monto_total.moneda,
            fecha_creacion=fecha_creacion,
            fecha_actualizacion=fecha_actualizacion
        )
    
    # Esta es la función que corregimos en la respuesta anterior
    def dto_a_entidad(self, dto: PagoDTO) -> Pago:
        pago = Pago()
        pago.id_socio = uuid.UUID(dto.id_socio)
        pago.monto_total = Monto(valor=dto.monto_total, moneda=dto.moneda)

        pago.transacciones = []
        if dto.comisiones:
            for com_dto in dto.comisiones:
                # La entidad Transaccion es necesaria aquí
                transaccion = Transaccion(
                   id_referencia=com_dto.id_referencia,
                   monto=Monto(com_dto.monto, com_dto.moneda),
                   descripcion=com_dto.descripcion
                )
                pago.transacciones.append(transaccion)
        
        return pago