import pytest
from unittest.mock import patch, MagicMock
from envio_bronze.bronze_handler import enviar_para_bronze, limpar_nan

def test_limpar_nan():

    import numpy as np
    dados = {
        "valor1": np.nan,
        "lista": [1, np.nan, 3],
        "dict": {"chave": np.nan, "outra_chave": 5}
    }
    resultado = limpar_nan(dados)
    assert resultado["valor1"] is None
    assert resultado["lista"][1] is None
    assert resultado["dict"]["chave"] is None

def test_enviar_para_bronze_sucesso():

    with patch("envio_bronze.bronze_handler.supabase.table") as mock_table:
        mock_table.return_value.insert.return_value.execute.return_value = MagicMock(data=[{"id": 1}])
        
        enviar_para_bronze({"teste": "dados"})
        
        mock_table.return_value.insert.assert_called_once()

def test_enviar_para_bronze_falha():
    with patch("envio_bronze.bronze_handler.supabase.table", side_effect=Exception("Erro no Supabase")), \
         patch("envio_bronze.bronze_handler.log_event") as mock_log: 

        enviar_para_bronze({"teste": "dados"})


        mock_log.assert_called_with(
            status=500, service="enviar_para_bronze",
            error_description="Erro no Supabase",
            level_type="ERROR", context="erro_controlado",
            latency_ms=pytest.approx(0, abs=5000) 
        )
