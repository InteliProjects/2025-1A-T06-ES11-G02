import pytest
from unittest.mock import patch, MagicMock
from consumer.consumer import callback, iniciar_consumidor

def test_callback_sucesso():

    mock_ch = MagicMock()
    mock_method = MagicMock()
    mock_properties = MagicMock()
    mock_body = b'{"dados": {"campo": "valor"}, "fonte": "Bronze"}'

    with patch("consumer.consumer.enviar_para_bronze") as mock_enviar_bronze, \
         patch("consumer.consumer.log_event") as mock_log_event:

        callback(mock_ch, mock_method, mock_properties, mock_body)

        mock_enviar_bronze.assert_called_once()
        mock_log_event.assert_called()

def test_callback_mensagem_invalida():

    mock_ch = MagicMock()
    mock_method = MagicMock()
    mock_properties = MagicMock()
    mock_body = b'invalido'

    with patch("consumer.consumer.log_event") as mock_log_event:
        callback(mock_ch, mock_method, mock_properties, mock_body)

        mock_log_event.assert_called()

def test_iniciar_consumidor():
    with patch("consumer.consumer.conectar_rabbitmq") as mock_conectar, \
         patch("consumer.consumer.log_event") as mock_log:


        mock_connection = MagicMock()
        mock_channel = MagicMock()


        mock_conectar.return_value = (mock_connection, mock_channel)

 
        mock_channel.start_consuming = MagicMock()


        iniciar_consumidor()


        mock_conectar.assert_called_once()

        mock_channel.start_consuming.assert_called_once()
