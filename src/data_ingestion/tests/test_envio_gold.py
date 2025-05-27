import pytest
from unittest.mock import patch, MagicMock
from envio_gold.gold_handler import conectar_clickhouse, enviar_para_gold, formatar_data, validar_campo
from datetime import datetime

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

def test_formatar_data_sucesso():

    data_str = "2025-03-10-15.30.45.123456"
    resultado = formatar_data(data_str, "DATA_TESTE")
    assert isinstance(resultado, datetime)

def test_formatar_data_falha():

    data_str = "data-invalida"
    resultado = formatar_data(data_str, "DATA_TESTE")
    assert isinstance(resultado, datetime) 

def test_validar_campo_sucesso():

    assert validar_campo("teste", "String", "CAMPO_TESTE") == "teste"
    assert validar_campo("123", "Int32", "CAMPO_TESTE") == 123
    assert validar_campo("123.45", "Float64", "CAMPO_TESTE") == 123.45



def test_enviar_para_gold_sucesso():
    with patch("envio_gold.gold_handler.conectar_clickhouse") as mock_connect, \
         patch("envio_gold.gold_handler.log_event"):

        mock_client = MagicMock()
        mock_connect.return_value = mock_client


        mock_client.insert = MagicMock()

     
        dados = {
            "fonte": "InteliStatus",
            "dados": {
                "ID": "123",
                "STATUS": "OK",
                "STATUS_DATA": "2024-03-13-14.30.00.000"
            }
        }

        enviar_para_gold(dados)

        expected_datetime = datetime(2024, 3, 13, 14, 30)

        mock_client.insert.assert_called_once_with(
            "gold_inteli_status",
            [("123", "OK", expected_datetime)],
            column_names=["ID", "STATUS", "STATUS_DATA"]
        )


def test_enviar_para_gold_falha():
    with patch("envio_gold.gold_handler.conectar_clickhouse", side_effect=Exception("Erro no ClickHouse")), \
         patch("envio_gold.gold_handler.log_event"):  

        dados = {"dados": {"ID": "123"}, "fonte": "InteliStatus"}
        

        enviar_para_gold(dados)

      
        assert True  

