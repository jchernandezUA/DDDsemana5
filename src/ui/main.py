
import asyncio
import websockets
import json
import logging
from threading import Thread

from alpespartners.consumidor import obtener_suscripcion_a_topico

logging.basicConfig(level=logging.INFO)
CLIENTES_CONECTADOS = set()

async def registrar_cliente(websocket):
    CLIENTES_CONECTADOS.add(websocket)
    logging.info(f"Nuevo cliente conectado: {websocket.remote_address}. Total clientes: {len(CLIENTES_CONECTADOS)}")

async def desregistrar_cliente(websocket):
    CLIENTES_CONECTADOS.remove(websocket)
    logging.info(f"Cliente desconectado: {websocket.remote_address}. Total clientes: {len(CLIENTES_CONECTADOS)}")

async def manejador_de_clientes(websocket, path):
    await registrar_cliente(websocket)
    try:
        await websocket.wait_closed()
    finally:
        await desregistrar_cliente(websocket)

# <<-- CAMBIO 1: La función ahora acepta el 'loop' como argumento -->>
def consumir_eventos_pulsar(loop):
    try:
        consumidor = obtener_suscripcion_a_topico()
        logging.info("Consumidor de Pulsar iniciado y escuchando...")
        
        while True:
            mensaje = consumidor.receive()
            try:
                # <<-- CAMBIO 2: Accedemos al payload con ['data'] -->>
                datos = mensaje.value()['data']
                json_datos = json.dumps(str(datos))
                logging.info(f"Evento recibido de Pulsar: {datos}")

                # <<-- CAMBIO 3: Usamos el 'loop' que nos pasaron como argumento -->>
                asyncio.run_coroutine_threadsafe(
                    enviar_mensaje_a_clientes(json_datos),
                    loop
                )
                
                consumidor.acknowledge(mensaje)
            except Exception as e:
                logging.error(f"Error procesando mensaje de Pulsar: {e}")
                consumidor.negative_acknowledge(mensaje)

    except Exception as e:
        logging.error(f"Error fatal en el consumidor de Pulsar: {e}")

async def enviar_mensaje_a_clientes(mensaje: str):
    if CLIENTES_CONECTADOS:
        tasks = [cliente.send(mensaje) for cliente in CLIENTES_CONECTADOS]
        await asyncio.gather(*tasks)
        logging.info(f"Mensaje enviado a {len(CLIENTES_CONECTADOS)} cliente(s).")

async def main():
    logging.info("========= Comenzando Servidor WebSocket en localhost:5678 =========")
    servidor = await websockets.serve(manejador_de_clientes, "localhost", 5678)
    await servidor.wait_closed()


if __name__ == "__main__":
    
    
    loop = asyncio.get_event_loop()

    # <<-- CAMBIO 4: Pasamos el 'loop' como argumento al crear el hilo -->>
    hilo_consumidor = Thread(target=consumir_eventos_pulsar, args=(loop,), daemon=True)
    hilo_consumidor.start()

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.info("Servidor detenido manualmente.")
    finally:
        loop.close()
        logging.info("Loop de eventos cerrado.")