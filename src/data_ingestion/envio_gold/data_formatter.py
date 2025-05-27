import time
from datetime import datetime
from logger.logger import log_event

def formatar_data(data_str, campo, origem="desconhecida"):
    if data_str is None:
        log_event(
            status=None, service="formatar_data",
            error_description=f"Campo {campo} está ausente ou nulo. Origem: {origem}",
            level_type="WARNING", context="validação"
        )
        return None  

    try:
        if isinstance(data_str, str):
            return datetime.strptime(data_str, "%Y-%m-%d-%H.%M.%S.%f")
        elif isinstance(data_str, datetime):
            return data_str
        raise ValueError(f"Formato inválido para {campo}")
    except (ValueError, TypeError) as e:
        log_event(
            status=None, service="formatar_data",
            error_description=f"Erro ao formatar {campo}: {e}. Dado recebido: '{data_str}' (Origem: {origem})",
            level_type="ERROR", context="validação"
        )
        return None  


def validar_campo(valor, tipo, campo, origem="desconhecida"):
    try:
        if tipo == "String":
            return str(valor)
        elif tipo == "Int32":
            return int(valor)
        elif tipo == "Float64":
            return float(valor)
        elif tipo == "DateTime":
            return formatar_data(valor, campo, origem)
    except (ValueError, TypeError) as e:
        log_event(
            status=None, service="validar_campo",
            error_description=f"Erro na conversão de {campo}: {e}. Dado recebido: '{valor}' (Origem: {origem})",
            level_type="ERROR", context="validação de dados" )
        return None
