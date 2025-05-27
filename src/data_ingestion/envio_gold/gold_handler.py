import time
from logger.logger import log_event
from envio_gold.data_formatter import validar_campo
from clickhouse.clickhouse_handler import inserir_no_clickhouse

TABELAS_GOLD = {
    "InteliResultados": {
        "tabela": "gold_inteli_resultados",
        "colunas": ["ID", "RESULT_ID", "CAPTURE_TIME", "STATUS"],
        "tipos": ["String", "String", "DateTime", "String"]
    },
    "InteliVeiculo": {
        "tabela": "gold_inteli_veiculo",
        "colunas": ["ID", "MODELL", "FARBAU", "FARBIN", "PR"],
        "tipos": ["String", "String", "String", "String", "String"]
    },
    "InteliFalhas": {
        "tabela": "gold_inteli_falhas",
        "colunas": ["ID", "DATA_DETECCAO", "PONTO", "LOC_ID", "POS_ID", "TYPE_ID", "VIEW_ID"],
        "tipos": ["String", "DateTime", "String", "Int32", "Int32", "Int32", "Float64"]
    },
    "InteliStatus": {
        "tabela": "gold_inteli_status",
        "colunas": ["ID", "STATUS", "STATUS_DATA"],
        "tipos": ["String", "String", "DateTime"]
    }
}

def enviar_para_gold(dados):
    start_time = time.time()
    fonte = dados.get("fonte", "desconhecida")
    conteudo = dados.get("dados", {})

    log_event(
        status=200, service="enviar_para_gold",
        error_description=f"Processando dados da fonte: {fonte}",
        level_type="SUCCESS", context="envio"
    )

    if fonte in TABELAS_GOLD:
        info = TABELAS_GOLD[fonte]
        tabela, colunas, tipos = info["tabela"], info["colunas"], info["tipos"]

        dados_formatados = [
            validar_campo(conteudo.get(col), tipo, col, fonte) for col, tipo in zip(colunas, tipos)
        ]

        if None not in dados_formatados:
            inserir_no_clickhouse(tabela, dados_formatados, colunas)
    else:
        log_event(
            status=500, service="enviar_para_gold",
            error_description=f"Fonte desconhecida: {fonte}",
            level_type="ERROR", context="envio"
        )
