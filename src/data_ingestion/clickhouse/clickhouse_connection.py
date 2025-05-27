import clickhouse_connect
from config import settings
from logger.logger import log_event
import time

client = None  # Criar um cliente global para reuso

def conectar_clickhouse():
    global client
    start_time = time.time()
    if client is not None:
        return client  # Retorna a conexão existente

    try:
        client = clickhouse_connect.get_client(
            host=settings.CLICKHOUSE_HOST,
            user=settings.CLICKHOUSE_USER,
            password=settings.CLICKHOUSE_PASSWORD,
            secure=settings.CLICKHOUSE_SECURE
        )
        log_event(
            status=200, service="conectar_clickhouse",
            error_description="Conexão com ClickHouse estabelecida.",
            level_type="SUCCESS", context="conexão com supabase",
            latency_ms=int((time.time() - start_time) * 1000)
        )
        return client
    except Exception as e:
        log_event(
            status=500, service="conectar_clickhouse",
            error_description=f"Erro ao conectar ao ClickHouse: {e}",
            level_type="ERROR", context="conexão com supabase",
            latency_ms=int((time.time() - start_time) * 1000)
        )
        raise
