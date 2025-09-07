"""
Script principal para ejecutar el módulo de notificaciones de forma independiente.
Este script puede usarse para probar el módulo o ejecutar los consumidores.
"""

import logging
from modulos.notificaciones.infraestructura.consumidores import iniciar_consumidores_notificaciones

def main():
    """Función principal del módulo de notificaciones."""
    print("=" * 80)
    print("🔔 INICIANDO MÓDULO DE NOTIFICACIONES")
    print("=" * 80)
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        # Iniciar consumidores de eventos
        iniciar_consumidores_notificaciones()
    except Exception as e:
        logging.error(f"Error ejecutando módulo de notificaciones: {str(e)}")
        raise

if __name__ == "__main__":
    main()
