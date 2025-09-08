# Alpespartners

Repositorio del sistema Alpespartners, una plataforma modular para la gestión de pagos, notificaciones y UI, basada en arquitectura hexagonal y comunicación asíncrona mediante eventos.

Este proyecto está diseñado para ser escalable y desacoplado, permitiendo la integración de nuevos servicios y adaptadores fácilmente.


## Arquitectura

La arquitectura de Alpespartners se basa en microservicios y módulos independientes:

- **API**: Exposición de endpoints para pagos y notificaciones.
- **Notificaciones**: Servicio dedicado para el manejo y envío de notificaciones.
- **UI**: Interfaz gráfica y servidor websocket para interacción en tiempo real.

La comunicación entre servicios se realiza mediante eventos y mensajes, permitiendo escalabilidad y resiliencia.

## Estructura completa del proyecto

A continuación se presenta el desglose detallado de la estructura del proyecto, explicando el propósito de cada carpeta y archivo, y su relación con la arquitectura hexagonal, DDD y la arquitectura basada en eventos:

```
Raíz del proyecto
├── aeropartners.Dockerfile         # Dockerfile para construir la imagen del servicio API
├── docker-compose.yml              # Orquestación de servicios y dependencias (DB, brokers, etc)
├── estructura_proyecto.txt         # Descripción de la estructura del proyecto
├── init-db.sql                     # Script de inicialización de la base de datos
├── notificacion-requirements.txt   # Dependencias Python para el servicio de notificaciones
├── notificacion.Dockerfile         # Dockerfile para el servicio de notificaciones
├── pyproject.toml                  # Configuración de proyecto Python (dependencias, metadata, etc)
├── README.md                       # Documentación general del proyecto
├── requirements.txt                # Dependencias globales Python
├── ui-requirements.txt             # Dependencias Python para el servicio UI
├── ui.Dockerfile                   # Dockerfile para el servicio UI
├── src/
│   ├── alpespartners/
│   │   ├── api/                    # Endpoints REST, entrada principal de la aplicación
│   │   │   ├── notificaciones.py   # Controlador REST para notificaciones
│   │   │   ├── pagos.py            # Controlador REST para pagos
│   │   ├── config/                 # Configuración general y acceso a la base de datos
│   │   │   ├── db.py               # Configura la conexión a la base de datos
│   │   │   ├── uow.py              # Implementa el patrón Unit of Work
│   │   ├── modulos/
│   │   │   ├── notificaciones/     # Lógica de negocio para notificaciones
│   │   │   │   ├── aplicacion/     # Casos de uso, comandos, servicios de aplicación
│   │   │   │   ├── dominio/        # Entidades, agregados, eventos de dominio, reglas de negocio
│   │   │   │   └── infraestructura/# Adaptadores para persistencia y brokers de eventos
│   │   │   ├── pagos/              # Lógica de negocio para pagos
│   │   │   │   ├── __init__.py     # Inicializa el módulo
│   │   │   │   ├── aplicacion/     # Casos de uso, comandos, servicios de aplicación
│   │   │   │   ├── dominio/        # Entidades, agregados, eventos de dominio, reglas de negocio
│   │   │   │   └── infraestructura/# Adaptadores para persistencia y brokers de eventos
│   │   ├── seedwork/               # Componentes compartidos, utilidades y patrones comunes
│   │   │   ├── __init__.py         # Inicializa el módulo seedwork
│   │   │   ├── aplicacion/         # Comandos, DTOs, servicios y handlers genéricos
│   │   │   ├── dominio/            # Entidades base, eventos, excepciones, fábricas, mixins, objetos de valor, reglas, repositorios y servicios compartidos
│   │   │   ├── infraestructura/    # Adaptadores genéricos para persistencia y mensajería
│   │   │   └── presentacion/       # Adaptadores para exponer la funcionalidad (API, CLI, UI)
│   ├── ui/                         # Interfaz gráfica web y servidor websocket
│   │   ├── __init__.py             # Inicializa el módulo UI
│   │   ├── main.py                 # Servidor websocket principal
│   │   ├── alpespartners/          # Lógica específica de la UI
│   │   │   ├── __init__.py         # Inicializa el submódulo
│   │   │   ├── consumidor.py       # Consume eventos y actualiza la UI
│   │   │   ├── publicador.py       # Publica eventos desde la UI
│   │   │   ├── utils.py            # Funciones auxiliares para la UI y eventos
│   │   │   └── vistas/             # Componentes gráficos y vistas de la interfaz web
|
```

### Relación con la arquitectura hexagonal, DDD y eventos

- **Hexagonal**: Cada módulo (pagos, notificaciones, UI) está dividido en capas de dominio, aplicación e infraestructura. Los adaptadores (infraestructura/presentación) permiten la integración con sistemas externos y la exposición de APIs, siguiendo el patrón de puertos y adaptadores.
- **DDD**: El dominio de cada módulo define entidades, agregados, objetos de valor y eventos, encapsulando la lógica central y las reglas de negocio. La capa de aplicación orquesta casos de uso y comandos, mientras que la infraestructura implementa la persistencia y la integración con brokers de eventos.
- **Eventos**: La comunicación entre servicios se realiza mediante eventos y mensajes, permitiendo la integración desacoplada, la escalabilidad y la resiliencia. Los módulos publican y consumen eventos a través de brokers, y la UI se actualiza en tiempo real mediante websockets.

Esta estructura facilita la extensibilidad, el desacoplamiento y la mantenibilidad del sistema, permitiendo agregar nuevos servicios y adaptadores sin afectar el núcleo de negocio.





## Ejecución de servicios

### API Alpespartners

```bash
flask --app src/alpespartners/api run --port=5000
```

### UI Websocket Server

```bash
python src/ui/main.py
```

### Crear imagen Docker

```bash
docker build . -f notificacion.Dockerfile -t alpespartners/notificacion
docker build . -f ui.Dockerfile -t alpespartners/ui
```

### Ejecutar contenedores (sin compose)

```bash
docker run alpespartners/notificacion
docker run alpespartners/ui
```



## Docker-compose

Para desplegar toda la arquitectura de Alpespartners en un solo comando, usa `docker-compose` desde el directorio principal:

```bash
docker-compose --profile alpespartners --profile pulsar up
```

Para detener los servicios:

```bash
docker-compose stop
```

Para ejecutar en segundo plano:

```bash
docker-compose up -d
```


## Comandos útiles

### Listar contenedores en ejecución
```bash
docker ps
```

### Listar todas los contenedores
```bash
docker ps -a
```

### Parar contenedor
```bash
docker stop <id_contenedor>
```

### Eliminar contenedor
```bash
docker rm <id_contenedor>
```

### Listar imágenes
```bash
docker images
```

### Eliminar imágenes
```bash
docker rmi <id_imagen>
```

### Acceder a un contenedor
```bash
docker exec -it <id_contenedor> sh
```

### Kill proceso que está usando un puerto
```bash
fuser -k <puerto>/tcp
```