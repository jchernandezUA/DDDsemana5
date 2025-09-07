# Propósito: Transformar entre el Agregado Pago del dominio y el modelo de persistencia 
# Pago DTO (SQLAlchemy).

from seedwork.dominio.repositorios import Mapeador
from modulos.pagos.dominio.entidades import Pago, Transaccion
from modulos.pagos.dominio.objetos_valor import Monto, EstadoPago
from .dto import Pago as PagoDTO, Transaccion as TransaccionDTO

class MapeadorPago(Mapeador):

    def obtener_tipo(self) -> type:
        return Pago.__class__

    def entidad_a_dto(self, entidad: Pago) -> PagoDTO:
        pago_dto = PagoDTO()
        pago_dto.id = str(entidad.id)
        pago_dto.id_socio = str(entidad.id_socio)
        pago_dto.monto_total = entidad.monto_total.valor
        pago_dto.moneda = entidad.monto_total.moneda
        pago_dto.estado = str(entidad.estado.value)
        pago_dto.fecha_creacion = entidad.fecha_creacion
        pago_dto.fecha_actualizacion = entidad.fecha_actualizacion

        transacciones_dto = []
        for transaccion_entidad in entidad.transacciones:
            trans_dto = TransaccionDTO(
                id=str(transaccion_entidad.id),
                id_referencia=str(transaccion_entidad.id_referencia),
                monto=transaccion_entidad.monto.valor,
                moneda=transaccion_entidad.monto.moneda,
                descripcion=transaccion_entidad.descripcion
            )
            transacciones_dto.append(trans_dto)
        
        pago_dto.transacciones = transacciones_dto
        return pago_dto

    def dto_a_entidad(self, dto: PagoDTO) -> Pago:
        pago = Pago(
            id=dto.id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion
        )
        pago.id_socio = dto.id_socio
        pago.monto_total = Monto(dto.monto_total, dto.moneda)
        pago.estado = EstadoPago(dto.estado)

        pago.transacciones = []
        for trans_dto in dto.transacciones:
            trans_entidad = Transaccion(
                id=trans_dto.id,
                id_referencia=trans_dto.id_referencia,
                monto=Monto(trans_dto.monto, trans_dto.moneda),
                descripcion=trans_dto.descripcion
            )
            pago.transacciones.append(trans_entidad)

        return pago