import pytest
from unittest.mock import patch, MagicMock
from producer.producer import iniciar_producer

@patch("producer.producer.conectar_rabbitmq")
@patch("producer.producer.carregar_csv")
@patch("producer.producer.selecionar_linha_aleatoria")
def test_iniciar_producer(mock_selecionar, mock_carregar, mock_conectar):
    mock_channel = MagicMock()
    mock_conectar.return_value = (MagicMock(), mock_channel)
    mock_carregar.return_value = MagicMock(empty=False)

    def mock_selecionar_func(*args, **kwargs):
        nonlocal contador
        if contador >= 3:  
            raise KeyboardInterrupt
        contador += 1
        return {"teste": "dados"}

    contador = 0
    mock_selecionar.side_effect = mock_selecionar_func

    with patch("time.sleep", return_value=None): 
        try:
            iniciar_producer()
        except KeyboardInterrupt:
            pass  

    mock_conectar.assert_called_once()
    assert contador == 3 
