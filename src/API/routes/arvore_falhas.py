from fastapi import APIRouter, Query, HTTPException
from services.arvore_falha_service import get_pct_por_tipo, get_falhas_por_periodo, get_status_etapas
from datetime import datetime

router = APIRouter(
    prefix="/arvore-falhas",
    tags=["arvore-falhas"]
)

@router.get("/pct-por-tipo")
async def get_pct_por_tipo_route(
    data_inicio: str = Query(
        description="Data inicial no formato YYYY-MM-DD"
    ),
    data_fim: str = Query(
        description="Data final no formato YYYY-MM-DD"
    ),
    ponto: str = Query(
        description="Ponto a ser analisado"
    )
):
    """
    Retorna a porcentagem de falhas por tipo dentro de um período específico
    
    Args:
        data_inicio (str): Data inicial no formato YYYY-MM-DD
        data_fim (str): Data final no formato YYYY-MM-DD
        ponto (str): Ponto a ser analisado (ex: 'ZP7')
        
    Returns:
        dict: Dicionário contendo os dados formatados
    """
    try:
        # Validação do formato das datas
        try:
            data_inicio_dt = datetime.strptime(data_inicio, "%Y-%m-%d")
            data_fim_dt = datetime.strptime(data_fim, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Formato de data inválido. Use o formato YYYY-MM-DD"
            )
        
        # Validação da ordem das datas
        if data_inicio_dt > data_fim_dt:
            raise HTTPException(
                status_code=400,
                detail="A data inicial deve ser menor que a data final"
            )
        
        return await get_pct_por_tipo(data_inicio, data_fim, ponto)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/falhas-por-periodo")
async def get_falhas_por_periodo_route(
    data_inicio: str = Query(
        description="Data inicial no formato YYYY-MM-DD"
    ),
    data_fim: str = Query(
        description="Data final no formato YYYY-MM-DD"
    ),
    ponto: str = Query(
        description="Ponto de referência"
    ),
    type_id: int = Query(
        description="ID do tipo de falha a ser analisado"
    )
):
    """
    Retorna a contagem de falhas por período (manhã/tarde) para outros pontos baseado em falhas específicas
    
    Args:
        data_inicio (str): Data inicial no formato YYYY-MM-DD
        data_fim (str): Data final no formato YYYY-MM-DD
        ponto (str): Ponto de referência (ex: 'ZP7')
        type_id (int): ID do tipo de falha a ser analisado
        
    Returns:
        dict: Dicionário contendo os dados formatados
    """
    try:
        # Validação do formato das datas
        try:
            data_inicio_dt = datetime.strptime(data_inicio, "%Y-%m-%d")
            data_fim_dt = datetime.strptime(data_fim, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Formato de data inválido. Use o formato YYYY-MM-DD"
            )
        
        # Validação da ordem das datas
        if data_inicio_dt > data_fim_dt:
            raise HTTPException(
                status_code=400,
                detail="A data inicial deve ser menor que a data final"
            )
        
        return await get_falhas_por_periodo(data_inicio, data_fim, ponto, type_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status-etapas")
async def get_status_etapas_route(
    data_inicio: str = Query(
        description="Data inicial no formato YYYY-MM-DD"
    ),
    data_fim: str = Query(
        description="Data final no formato YYYY-MM-DD"
    ),
    ponto: str = Query(
        description="Ponto de referência"
    ),
    type_id: int = Query(
        description="ID do tipo de falha a ser analisado"
    )
):
    """
    Retorna a contagem de veículos por etapa de status (Armação, Pintura e Montagem)
    
    Args:
        data_inicio (str): Data inicial no formato YYYY-MM-DD
        data_fim (str): Data final no formato YYYY-MM-DD
        ponto (str): Ponto de referência (ex: 'ZP7')
        type_id (int): ID do tipo de falha a ser analisado
        
    Returns:
        dict: Dicionário contendo os dados formatados
    """
    try:
        # Validação do formato das datas
        try:
            data_inicio_dt = datetime.strptime(data_inicio, "%Y-%m-%d")
            data_fim_dt = datetime.strptime(data_fim, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Formato de data inválido. Use o formato YYYY-MM-DD"
            )
        
        # Validação da ordem das datas
        if data_inicio_dt > data_fim_dt:
            raise HTTPException(
                status_code=400,
                detail="A data inicial deve ser menor que a data final"
            )
        
        return await get_status_etapas(data_inicio, data_fim, ponto, type_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 