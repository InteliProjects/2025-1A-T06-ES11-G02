from fastapi import APIRouter, HTTPException
from services.falhas.falhas_service import get_falhas_dia,get_falhas_veiculos,get_veiculos_falhas,get_tipo_falhas
import os


router = APIRouter(
    prefix="/falhas",
    tags=["falhas"]
)

@router.get("/debug-env")
async def debug_env():
    """
    Endpoint para debug das variáveis de ambiente
    """
    return {
        "CLICKHOUSE_HOST": os.getenv('CLICKHOUSE_HOST'),
        "CLICKHOUSE_USER": os.getenv('CLICKHOUSE_USER'),
        "CLICKHOUSE_SECURE": os.getenv('CLICKHOUSE_SECURE')
    }

@router.get("/carros-afetados-por-dia")
async def get_carros_afetados_por_dia():
    """
    Retorna a contagem de carros únicos que apresentaram falhas por dia.
    Exemplo: Se um mesmo carro teve 3 falhas no mesmo dia, ele é contado apenas uma vez.
    """
    try:
        return await get_veiculos_falhas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/erros-por-modelo")
async def get_erros_por_modelo():
    """
    Retorna a contagem total de erros agrupados por modelo de veículo.
    Exemplo: Se um carro teve 3 falhas, ele é contado 3 vezes.
    """
    try:
        return await get_falhas_veiculos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/falhas-diarias")
async def get_falhas_diarias():
    """
    Retorna a contagem total de falhas por dia e a média geral.
    Inclui:
    - Contagem total de falhas por dia (não distinta)
    - Média geral de falhas por dia (total de falhas / total de dias)
    """
    try:
        return await get_falhas_dia()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/falhas-por-tipo")
async def get_falhas_por_tipo():
    """
    Retorna a contagem total de falhas agrupadas por tipo de falha.
    Exemplo: Quantas falhas de cada tipo ocorreram no total.
    """
    try:
        return await get_tipo_falhas()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    



