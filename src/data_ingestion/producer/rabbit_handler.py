import json
import time
from logger.logger import log_event
from rabbit_mq.connection import conectar_rabbitmq

def conectar_fila():
    """Estabelece conexão com o RabbitMQ e retorna a conexão e canal."""
    start_time = time.time()
    connection, channel = conectar_rabbitmq()

    if not connection or not channel:
        log_event(
            status=500, service="conectar_fila",
            error_description="Falha ao conectar ao RabbitMQ.",
            level_type="ERROR", context="conexão",
            latency_ms=int((time.time() - start_time) * 1000)
        )
        return None, None

    log_event(
        status=200, service="conectar_fila",
        error_description="Conectado ao RabbitMQ.",
        level_type="SUCCESS", context="conexão",
        latency_ms=int((time.time() - start_time) * 1000)
    )

    return connection, channel

def enviar_para_fila(mensagem, channel):
    """Publica uma mensagem na fila do RabbitMQ."""
    envio_start = time.time()

    try:
        mensagem_json = json.dumps(mensagem)
        channel.basic_publish(exchange='', routing_key="fila_ingestao", body=mensagem_json)

        log_event(
            status=200, service="enviar_para_fila",
            error_description=f"Mensagem enviada para a fila: {mensagem['fonte']}",
            level_type="SUCCESS", context="envio",
            latency_ms=int((time.time() - envio_start) * 1000)
        )

    except Exception as e:
        log_event(
            status=500, service="enviar_para_fila",
            error_description=f"Erro ao enviar mensagem para fila: {str(e)}",
            level_type="ERROR", context="envio",
            latency_ms=int((time.time() - envio_start) * 1000)
        )
