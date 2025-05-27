import time
from envio_bronze.bronze_handler import enviar_para_bronze
from envio_prata.prata_handler import enviar_para_prata
from envio_gold.gold_handler import enviar_para_gold
from logger.logger import log_event

def processar_dados(dados):

    processos = {
        "Bronze": enviar_para_bronze,
        "Prata": enviar_para_prata,
        "Gold": enviar_para_gold
    }

    status_envios = {}
    for nome, func in processos.items():
        envio_start = time.time()
        try:
            func(dados)
            status_envios[nome] = 200
        except Exception as e:
            status_envios[nome] = None  
            log_event(
                status=None, service=f"enviar_para_{nome.lower()}",
                error_description=str(e),
                level_type="ERROR", context="envio",
                latency_ms=int((time.time() - envio_start) * 1000)
            )

    return status_envios
