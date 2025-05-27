import json
import time
import sys
from consumer.message_handler import decodificar_mensagem
from consumer.process_handler import processar_dados
from consumer.rabbit_handler import iniciar_consumidor
from logger.logger import log_event

contador = 0

def callback(ch, method, properties, body):
    """Callback chamado ao receber uma mensagem da fila."""
    global contador
    start_time = time.time()

    try:
        dados, context = decodificar_mensagem(body)

        if dados is None:
            raise ValueError("Erro na mensagem recebida.")

        log_event(
            status=200, service="consumer_callback",
            error_description="Mensagem recebida com sucesso.",
            level_type="SUCCESS", context=context,
            latency_ms=int((time.time() - start_time) * 1000)
        )

        status_envios = processar_dados(dados)

        log_event(
            status=200 if all(v == 200 for v in status_envios.values()) else None,
            service="consumer_callback",
            error_description=f"Processamento finalizado | Bronze: {status_envios['Bronze']} | Prata: {status_envios['Prata']} | Gold: {status_envios['Gold']}",
            level_type="SUCCESS" if all(v == 200 for v in status_envios.values()) else "WARNING",
            context="envio",
            latency_ms=int((time.time() - start_time) * 1000)
        )

        contador += 1
        sys.stdout.write(f"\rMensagens processadas: {contador} ")
        sys.stdout.flush()

    except Exception as e:
        log_event(
            status=None, service="consumer_callback",
            error_description=str(e),
            level_type="ERROR", context="erro geral",
            latency_ms=int((time.time() - start_time) * 1000)
        )

if __name__ == "__main__":
    iniciar_consumidor(callback)
