import pika
import time
from config import settings
from logger.logger import log_event  

def conectar_rabbitmq():
    max_attempts = 3
    retry_delay = 0 
    attempt = 0
    start_time = time.time() 

    while attempt < max_attempts:
        try:
            print(f"[RABBITMQ] Tentando conectar ao RabbitMQ... (Tentativa {attempt + 1}/{max_attempts})")
            connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue=settings.RABBITMQ_QUEUE)
            print("Conectado com sucesso!")
            log_event(
                status=200, service="conectar_rabbitmq",
                error_description="Conectado ao RabbitMQ.",
                level_type="SUCCESS", context="conexão com rabbitmq",
                latency_ms=int((time.time() - start_time) * 1000)
            )
            return connection, channel 

        except pika.exceptions.AMQPConnectionError as e:
            attempt += 1
            print(f"[RABBITMQ] Erro ao conectar! Tentando novamente em {retry_delay} segundos...")
            log_event(
                status=500, service="conectar_rabbitmq",
                error_description=f"Erro de conexão: {e}",
                level_type="ERROR", context="conexão com rabbitmq",
                latency_ms=int((time.time() - start_time) * 1000)
            )
            time.sleep(retry_delay)

    print(f"[RABBITMQ] Falha ao conectar após {max_attempts} tentativas.")
    log_event(
        status=500, service="conectar_rabbitmq",
        error_description="Falha ao conectar após várias tentativas.",
        level_type="ERROR", context="conexão com rabbitmq",
        latency_ms=int((time.time() - start_time) * 1000)
    )
    return None, None
