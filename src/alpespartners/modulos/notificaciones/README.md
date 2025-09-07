# Módulo de Notificaciones

Este módulo maneja el envío de notificaciones por email cuando ocurren eventos relacionados con pagos.

## Funcionalidad

- **Escucha eventos de pagos**: Se suscribe a eventos `PagoCreado`, `PagoProcesado`, y `PagoRechazado`
- **Crea notificaciones automáticas**: Genera notificaciones cuando detecta eventos de pagos
- **Simula envío de emails**: Utiliza logs para simular el envío de correos electrónicos
- **Publica eventos propios**: Emite eventos `NotificacionCreada`, `NotificacionEnviada`, `NotificacionFallida`

## Arquitectura

### Dominio
- **Entidades**: `Notificacion` (Agregado Raíz)
- **Objetos de Valor**: `DestinatarioEmail`, `TipoNotificacion`, `EstadoNotificacion`, `ContenidoNotificacion`
- **Eventos**: `NotificacionCreada`, `NotificacionEnviada`, `NotificacionFallida`
- **Repositorios**: Interface `RepositorioNotificaciones`

### Aplicación  
- **DTOs**: `NotificacionDTO`, `ContenidoDTO`
- **Handlers**: Manejo de eventos de dominio y eventos de pagos
- **Mapeadores**: Conversión entre entidades y DTOs

### Infraestructura
- **Persistencia**: Modelo SQLAlchemy para notificaciones
- **Messaging**: Consumidores y despachadores para Pulsar
- **Servicios**: `ServicioEmail` para simular envío de correos
- **Schemas**: Definiciones Avro para eventos

## Uso

```python
# Ejecutar el módulo independientemente
python -m aeroalpes.modulos.notificaciones.main

# O importar para usar en otros módulos
from aeroalpes.modulos.notificaciones.aplicacion.handlers import HandlerEventosPago
```

## Eventos que consume

- `eventos-pago`: Escucha eventos del módulo de pagos

## Eventos que produce

- `eventos-notificacion`: Publica eventos de notificaciones
