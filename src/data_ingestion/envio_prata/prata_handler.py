import time
import json
from config import settings
from logger.logger import log_event
from clickhouse.clickhouse_connection import conectar_clickhouse

def enviar_para_prata(dados):
    start_time = time.time()

    try:
        if not isinstance(dados, dict):
            log_event(
                status=500, service="enviar_para_prata",
                error_description="Erro: Dados recebidos não são um dicionário.",
                level_type="ERROR", context="validação"
            )
            return

        json_content = json.dumps(dados, ensure_ascii=False)
        tag = str(dados.get("fonte", "desconhecida"))

        client = conectar_clickhouse()
        if client is None:
            log_event(
                status=500, service="enviar_para_prata",
                error_description="Erro: Falha na conexão com ClickHouse.",
                level_type="ERROR", context="conexão"
            )
            return

        client.insert(
            "default.prata_events",
            [(json_content, tag)],
            column_names=["json_content", "tag"]
        )

        log_event(
            status=200, service="enviar_para_prata",
            error_description="Dados inseridos na camada Prata com sucesso.",
            level_type="SUCCESS", context="envio",
            latency_ms=int((time.time() - start_time) * 1000)
        )

    except Exception as e:
        log_event(
            status=500, service="enviar_para_prata",
            error_description=f"Erro ao inserir na camada Prata: {str(e)}",
            level_type="ERROR", context="envio",
            latency_ms=int((time.time() - start_time) * 1000)
        )
