import pytest
from unittest.mock import patch, MagicMock
from envio_prata.prata_handler import conectar_clickhouse, enviar_para_prata

def test_conectar_clickhouse_sucesso():

    with patch("clickhouse_connect.get_client") as mock_client:
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        
        client = conectar_clickhouse()
        
        assert client is not None
        mock_client.assert_called_once()

def test_conectar_clickhouse_falha():

    with patch("clickhouse_connect.get_client", side_effect=Exception("Erro de conexão")):
        with pytest.raises(Exception):
            conectar_clickhouse()

def test_enviar_para_prata_sucesso():

    with patch("envio_prata.prata_handler.conectar_clickhouse") as mock_connect:
        mock_client = MagicMock()
        mock_connect.return_value = mock_client
        
        dados = {"teste": "dados", "fonte": "teste"}
        enviar_para_prata(dados)
        
        mock_client.insert.assert_called_once()

def test_enviar_para_prata_falha():
    with patch("envio_prata.prata_handler.conectar_clickhouse", side_effect=Exception("Erro no ClickHouse")), \
         patch("envio_prata.prata_handler.log_event") as mock_log: 

        enviar_para_prata({"teste": "dados", "fonte": "teste"})


        mock_log.assert_called_with(
            status=500, service="enviar_para_prata",
            error_description="Erro no ClickHouse",
            level_type="ERROR", context="envio",
            latency_ms=pytest.approx(0, abs=5000) 
        )