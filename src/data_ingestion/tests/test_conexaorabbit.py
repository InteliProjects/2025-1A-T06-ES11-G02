import pytest
from unittest.mock import patch, MagicMock
import pika
from rabbit_mq.connection import conectar_rabbitmq

def test_conexao_sucesso():

    with patch("pika.BlockingConnection") as mock_connection:
        mock_channel = MagicMock()
        mock_connection.return_value.channel.return_value = mock_channel

        connection, channel = conectar_rabbitmq()
        
        assert connection is not None
        assert channel is not None
        mock_connection.assert_called_once()
        mock_channel.queue_declare.assert_called_once()

def test_conexao_falha():
    with patch("pika.BlockingConnection", side_effect=pika.exceptions.AMQPConnectionError("Erro de conexão")):
        with patch("rabbit_mq.connection.log_event"):  
            connection, channel = conectar_rabbitmq()
            

            assert connection is None
            assert channel is None
