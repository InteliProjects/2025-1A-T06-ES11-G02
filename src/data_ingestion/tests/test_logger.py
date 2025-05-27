import pytest
from unittest.mock import patch, MagicMock
from logger.logger import log_event

def test_log_event_success():

    with patch("logger.logger.supabase.table") as mock_table:
        mock_table.return_value.insert.return_value.execute.return_value = MagicMock(data=[{"id": 1}])
        
        log_event(status=200, service="test_service", error_description=None, level_type="SUCCESS", latency_ms=100, context="test")
        
        mock_table.return_value.insert.assert_called_once()

def test_log_event_error():

    with patch("logger.logger.supabase.table") as mock_table:
        mock_table.return_value.insert.return_value.execute.return_value = MagicMock(data=[{"id": 1}])
        
        log_event(status=500, service="test_service", error_description="Erro simulado", level_type="ERROR", latency_ms=100, context="test")
        
        mock_table.return_value.insert.assert_called_once()

def test_log_event_invalid_level():

    with patch("logger.logger.supabase.table") as mock_table:
        mock_table.return_value.insert.return_value.execute.return_value = MagicMock(data=[{"id": 1}])
        
        log_event(status=200, service="test_service", error_description=None, level_type="INVALID", latency_ms=100, context="test")
        
        mock_table.return_value.insert.assert_called_once()
