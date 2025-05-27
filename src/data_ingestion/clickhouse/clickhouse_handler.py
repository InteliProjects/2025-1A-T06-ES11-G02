import time
from clickhouse.clickhouse_connection import conectar_clickhouse
from logger.logger import log_event

def inserir_no_clickhouse(tabela, dados, colunas):

    start_time = time.time()
    try:
        client = conectar_clickhouse()
        client.insert(tabela, [dados], column_names=colunas)

        log_event(
            status=200, service="inserir_no_clickhouse",
            error_description=f"Dados inseridos na tabela {tabela}.",
            level_type="SUCCESS", context="envio",
            latency_ms=int((time.time() - start_time) * 1000)
        )
    except Exception as e:
        log_event(
            status=500, service="inserir_no_clickhouse",
            error_description=f"Erro ao inserir dados na tabela {tabela}: {e}",
            level_type="ERROR", context="envio",
            latency_ms=int((time.time() - start_time) * 1000)
        )
