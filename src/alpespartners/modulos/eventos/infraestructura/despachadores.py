"""
Despachadores de eventos para el módulo de Eventos
"""
from datetime import datetime

epoch = datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        ...

    def publicar_evento(self, evento, topico):
        ...