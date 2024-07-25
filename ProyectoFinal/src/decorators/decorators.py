
import time  # Importa el módulo time para medir el tiempo de ejecución.
import logging  # Importa el módulo logging para registrar mensajes.

# Configurar el logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

"""
Configura el registro de mensajes (logging) para que muestre mensajes de nivel INFO y superior.
Define el formato de los mensajes de registro, incluyendo la marca de tiempo (asctime), el nivel del mensaje (levelname) y el mensaje en sí (message).
"""

def timeit(func):
    """Decorador para medir el tiempo de ejecución de una función."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registra el tiempo de inicio
        result = func(*args, **kwargs)  # Ejecuta la función decorada
        end_time = time.time()  # Registra el tiempo de finalización
        elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds")  # Registra el tiempo de ejecucion
        return result  # Devuelve el resultado de la funcion
    return wrapper  # Devuelve el decorador

def logit(func):
    """Decorador para registrar la ejecucion de una funcion."""
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")  # Registra el inicio de la ejecución de la funcion
        result = func(*args, **kwargs)  # Ejecuta la función decorada
        logging.info(f"Completado {func.__name__}")  # Registra la finalización de la ejecución de la funcion
        return result  # Devuelve el resultado de la función
    return wrapper  # Devuelve el decorador