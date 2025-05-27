import pandas as pd
import time
from logger.logger import log_event

def carregar_csv(caminho_csv):

    start_time = time.time()
    try:
        df = pd.read_csv(caminho_csv)
        log_event(
            status=200, service="carregar_csv",
            error_description=f"CSV carregado: {caminho_csv} - {len(df)} linhas.",
            level_type="SUCCESS", context="leitura de dados",
            latency_ms=int((time.time() - start_time) * 1000)
        )


        if df.isnull().sum().sum() > 0:
            log_event(
                status=200, service="carregar_csv",
                error_description=f"CSV {caminho_csv} contém campos ausentes, mas será processado.",
                level_type="WARNING", context="validação de dados",
                latency_ms=int((time.time() - start_time) * 1000)
            )

        return df

    except Exception as e:
        log_event(
            status=500, service="carregar_csv",
            error_description=f"Erro ao carregar CSV {caminho_csv}: {str(e)}",
            level_type="ERROR", context="leitura de dados",
            latency_ms=int((time.time() - start_time) * 1000)
        )
        return pd.DataFrame()  

def selecionar_linha_aleatoria(df):

    if df.empty:
        return None
    return df.sample(n=1).to_dict(orient='records')[0]
