import requests
import json
import os
import logging

from pulsar.schema import *
from fastavro.schema import parse_schema

PULSAR_ENV: str = 'PULSAR_ADDRESS'

def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")

def consultar_schema_registry(topico: str) -> dict:
    """
    Consulta el schema registry de Pulsar para un tópico.
    Maneja el caso en que el schema aún no exista.
    """
    try:
        response = requests.get(f'http://{broker_host()}:8080/admin/v2/schemas/{topico}/schema')
        # Lanza una excepción si la respuesta es un error (ej. 404 Not Found)
        response.raise_for_status()
        
        json_registry = response.json()
        # El schema real está en formato string dentro de la clave 'data'
        schema_string = json_registry.get('data')
        
        if schema_string:
            # Si encontramos el schema, lo parseamos desde su string
            return json.loads(schema_string)
        else:
            # Si la clave 'data' no existe, devolvemos un dict vacío
            return {}

    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        # Si la petición falla (ej. 404) o la respuesta no es JSON,
        # significa que el schema no existe. Devolvemos un dict vacío.
        logging.warning(f"No se pudo obtener el schema para el tópico '{topico}'. Error: {e}. Probablemente aún no ha sido creado. Se continuará sin schema.")
        return {}

def obtener_schema_avro_de_diccionario(json_schema: dict) -> AvroSchema:
    if not json_schema:
        # Si el schema está vacío, usamos un schema genérico que acepta cualquier cosa
        logging.warning("Schema no encontrado o vacío. Usando BytesSchema genérico.")
        return BytesSchema()
        
    definicion_schema = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=definicion_schema)