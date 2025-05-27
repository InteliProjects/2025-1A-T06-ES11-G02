import random
import math
import time
from supabase import create_client, Client
from config import settings
from logger.logger import log_event  


supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_API_KEY)

def limpar_nan(val):
    if isinstance(val, float) and math.isnan(val):
        return None
    elif isinstance(val, dict):
        return {k: limpar_nan(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [limpar_nan(v) for v in val]
    return val

def enviar_para_bronze(dados):
    try:
        start_time = time.time()  

        
        if random.random() < 0.1:
            raise ValueError("Erro controlado: Simulação de falha no envio para o Bronze.")

        
        dados_limpos = limpar_nan(dados)
        bronze_payload = {"raw_data": dados_limpos}

        
        response = supabase.table("bronze").insert(bronze_payload).execute()

        
        if hasattr(response, 'data') and response.data:
            log_event(
                status=200,
                service="enviar_para_bronze",
                error_description=None,
                level_type="SUCCESS",
                context="envio",
                latency_ms=int((time.time() - start_time) * 1000)
            )
        else:
            log_event(
                status=None,
                service="enviar_para_bronze",
                error_description=f"Resposta inesperada: {response}",
                level_type="WARNING",
                context="envio",
                latency_ms=int((time.time() - start_time) * 1000)
            )

    except Exception as e:
        log_event(
            status=500,
            service="enviar_para_bronze",
            error_description=str(e),
            level_type="ERROR",
            context="erro_controlado", 
            latency_ms=int((time.time() - start_time) * 1000)
        )
