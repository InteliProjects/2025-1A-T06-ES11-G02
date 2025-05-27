import time
import sys
from rabbit_mq.connection import conectar_rabbitmq
from logger.logger import log_event

contador = 0

def iniciar_consumidor(callback):

    global contador
    start_time = time.time()  

    connection, channel = conectar_rabbitmq()
    if connection and channel:
        log_event(
            status=200, service="iniciar_consumidor",
            error_description="Conectado ao RabbitMQ.",
            level_type="SUCCESS", context="conexão com supabase",
            latency_ms=int((time.time() - start_time) * 1000)
        )
        print("\nMensagens processadas:", end=" ", flush=True)
        channel.basic_consume(queue="fila_ingestao", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    else:
        log_event(
            status=None, service="iniciar_consumidor",
            error_description="Falha ao conectar ao RabbitMQ.",
            level_type="ERROR", context="conexão com supabase",
            latency_ms=int((time.time() - start_time) * 1000)
        )
