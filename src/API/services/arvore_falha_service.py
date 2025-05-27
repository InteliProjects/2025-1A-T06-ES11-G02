from config.connection import DatabaseConnection

async def get_pct_por_tipo(data_inicio: str, data_fim: str, ponto: str):
    """
    Retorna a porcentagem de falhas por tipo dentro de um período específico
    
    Args:
        data_inicio (str): Data inicial no formato YYYY-MM-DD
        data_fim (str): Data final no formato YYYY-MM-DD
        ponto (str): Ponto a ser analisado (ex: 'ZP7')
        
    Returns:
        dict: Dicionário contendo os dados formatados
    """
    db = DatabaseConnection()
    ponto = ponto.upper()  # Convertendo para maiúsculas
    
    query = """
    with specific_falhas as (
        SELECT
        registro_id
        FROM gold_inteli_falhas
        WHERE date("DATA DETECCAO") between date('{data_inicio}') AND date('{data_fim}')
        AND PONTO = '{ponto}'
    )
    , raw_data as (
        SELECT
        gold_inteli_falhas.TYPE_ID
        ,count(*) as contagem_erro
        FROM gold_inteli_falhas as falhas
        INNER JOIN specific_falhas as sf on falhas.registro_id = sf.registro_id
        GROUP BY 1
        ORDER BY 2 DESC
    )
    , total as (
        SELECT sum(contagem_erro) as universo_total
        FROM raw_data
    )
    SELECT
    *
    ,contagem_erro / (SELECT universo_total from total) as pct
    FROM raw_data
    ORDER BY 2 DESC
    LIMIT 10
    """.format(data_inicio=data_inicio, data_fim=data_fim, ponto=ponto)
    
    try:
        result = db.execute_query(query)
        
        # Formata o resultado
        formatted_result = [
            {
                'type_id': row[0],
                'contagem_erro': row[1],
                'pct': float(row[2])
            }
            for row in result[0]  # Acessando o primeiro elemento do resultado que contém os dados
        ]
        
        return {"data": formatted_result}
        
    except Exception as e:
        raise Exception(f"Erro ao buscar porcentagem de falhas por tipo: {str(e)}")

async def get_falhas_por_periodo(data_inicio: str, data_fim: str, ponto: str, type_id: int):
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
    db = DatabaseConnection()
    ponto = ponto.upper()  # Convertendo para maiúsculas
    
    query = """
    with raw_data as (
        SELECT DISTINCT 
        "ID"
        FROM
        gold_inteli_falhas
        WHERE date("DATA DETECCAO") between date('{data_inicio}') AND date('{data_fim}')
        AND PONTO = '{ponto}'
        AND TYPE_ID = {type_id}
    )
    ,grouped_data as (
    SELECT 
    PONTO
    ,TYPE_ID
    ,countIf(toHour("DATA DETECCAO") BETWEEN 0 AND 12) AS ContagemPeriodo1
    ,countIf(toHour("DATA DETECCAO") BETWEEN 13 AND 23) AS ContagemPeriodo2
    ,count(*) as contagem
    FROM gold_inteli_falhas
    WHERE date("DATA DETECCAO") BETWEEN date('{data_inicio}') AND date('{data_fim}')
    AND PONTO <> '{ponto}'
    AND "ID" IN (SELECT "ID" FROM raw_data )
    GROUP BY 1,2
    )
    , total_failures as (
        SELECT
        sum(contagem)  as total
        FROM grouped_data
    )
    ,final_data as (SELECT 
    PONTO
    ,TYPE_ID
    ,ContagemPeriodo1
    ,ContagemPeriodo2
    ,contagem
    ,contagem / (SELECT total from total_failures) as pct
    ,row_number() over (partition by PONTO order by contagem desc) as ranking
    FROM 
    grouped_data
    )
    SELECT * 
    FROM final_data 
    WHERE ranking <= 10
    order by PONTO,ranking
    """.format(data_inicio=data_inicio, data_fim=data_fim, ponto=ponto, type_id=type_id)
    
    try:
        result = db.execute_query(query)
        
        # Formata o resultado
        formatted_result = [
            {
                'ponto': row[0],
                'type_id': row[1],
                'contagem_periodo1': row[2],
                'contagem_periodo2': row[3],
                'contagem_total': row[4],
                'pct': float(row[5]),
                'ranking': row[6]
            }
            for row in result[0]  # Acessando o primeiro elemento do resultado que contém os dados
        ]
        
        return {"data": formatted_result}
        
    except Exception as e:
        raise Exception(f"Erro ao buscar falhas por período: {str(e)}")

async def get_status_etapas(data_inicio: str, data_fim: str, ponto: str, type_id: int):
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
    db = DatabaseConnection()
    ponto = ponto.upper()  # Convertendo para maiúsculas
    
    query = """
    with raw_data as (
        SELECT DISTINCT 
        "ID"
        FROM
        gold_inteli_falhas
        WHERE date("DATA DETECCAO") between date('{data_inicio}') AND date('{data_fim}')
        AND PONTO = '{ponto}'
        AND TYPE_ID = {type_id}
    )
    , periodos as (SELECT
    *
    , (case when toHour(STATUS_DATA) BETWEEN 6 AND 14 then 'P1'
           when toHour(STATUS_DATA) BETWEEN 15 AND 23 then 'P2'
           when toHour(STATUS_DATA) BETWEEN 0 AND 5 then 'P3'
      end) as periodo
    FROM
    gold_inteli_status
    WHERE ID IN (SELECT ID FROM raw_data)
    )
    , grouped_status as (
    SELECT
    ID
    ,STATUS
    ,periodo
    FROM periodos
    WHERE STATUS IN ('R100','R800','L100','L800','M100','G600')
    )
    , pivot_table as (
      SELECT
      ID
      ,anyIf(periodo, STATUS = 'R100') AS periodo_R100
      ,anyIf(periodo, STATUS = 'R800') AS periodo_R800
      ,anyIf(periodo, STATUS = 'L100') AS periodo_L100
      ,anyIf(periodo, STATUS = 'L800') AS periodo_L800
      ,anyIf(periodo, STATUS = 'M100') AS periodo_M100
      ,anyIf(periodo, STATUS = 'G600') AS periodo_G600
    FROM grouped_status
    GROUP BY ID
    )
    , final_data as (SELECT
    ID
    ,(case 
        when periodo_R100 = 'P1' AND periodo_R800 = 'P1' then '1T ARM'
        when periodo_R100 = 'P2' AND periodo_R800 = 'P2' THEN '2T ARM'
        when periodo_R100 = 'P3' AND periodo_R800 = 'P3' THEN '3T ARM'
        when (periodo_R100 is null OR periodo_R800 is null) then 'NO INFO ARM'
        else 'TROCA ARM'
      end
      ) as ARMACAO
    ,(case 
        when periodo_L100 = 'P1' AND periodo_L800 = 'P1' then '1T PINT'
        when periodo_L100 = 'P2' AND periodo_L800 = 'P2' THEN '2T PINT'
        when periodo_L100 = 'P3' AND periodo_L800 = 'P3' THEN '3T PINT'
        when (periodo_L100 is null OR periodo_L800 is null) then 'NO INFO PINT'
        else 'TROCA PINT'
      end
      ) as PINTURA
    ,(case 
        when periodo_M100 = 'P1' AND periodo_G600 = 'P1' then '1T MONT'
        when periodo_M100 = 'P2' AND periodo_G600 = 'P2' THEN '2T MONT'
        when periodo_M100 = 'P3' AND periodo_G600 = 'P3' THEN '3T MONT'
        when (periodo_M100 is null OR periodo_G600 is null) then 'NO INFO MONT'
        else 'TROCA MONT'
      end
      ) as MONTAGEM
    FROM pivot_table
    )
    SELECT
        countIf(ARMACAO IS NOT NULL) AS total_armacao,
        countIf(ARMACAO LIKE '1T ARM') AS armacao_t1,
        countIf(ARMACAO LIKE '2T ARM') AS armacao_t2,
        countIf(ARMACAO LIKE '3T ARM') AS armacao_t3,
        countIf(ARMACAO LIKE 'NO INFO%') AS armacao_sem_info,
        countIf(ARMACAO LIKE 'TROCA%') AS armacao_troca,

        countIf(PINTURA IS NOT NULL) AS total_pintura,
        countIf(PINTURA LIKE '1T PINT') AS pintura_t1,
        countIf(PINTURA LIKE '2T PINT') AS pintura_t2,
        countIf(PINTURA LIKE '3T PINT') AS pintura_t3,
        countIf(PINTURA LIKE 'NO INFO%') AS pintura_sem_info,
        countIf(PINTURA LIKE 'TROCA%') AS pintura_troca,

        countIf(MONTAGEM IS NOT NULL) AS total_montagem,
        countIf(MONTAGEM LIKE '1T MONT') AS montagem_t1,
        countIf(MONTAGEM LIKE '2T MONT') AS montagem_t2,
        countIf(MONTAGEM LIKE '3T MONT') AS montagem_t3,
        countIf(MONTAGEM LIKE 'NO INFO%') AS montagem_sem_info,
        countIf(MONTAGEM LIKE 'TROCA%') AS montagem_troca
    FROM final_data
    """.format(data_inicio=data_inicio, data_fim=data_fim, ponto=ponto, type_id=type_id)
    
    try:
        result = db.execute_query(query)
        
        # Formata o resultado
        row = result[0][0]  # Pegando a primeira (e única) linha do resultado
        formatted_result = {
            'armacao': {
                'total': row[0],
                'turno1': row[1],
                'turno2': row[2],
                'turno3': row[3],
                'sem_info': row[4],
                'troca': row[5]
            },
            'pintura': {
                'total': row[6],
                'turno1': row[7],
                'turno2': row[8],
                'turno3': row[9],
                'sem_info': row[10],
                'troca': row[11]
            },
            'montagem': {
                'total': row[12],
                'turno1': row[13],
                'turno2': row[14],
                'turno3': row[15],
                'sem_info': row[16],
                'troca': row[17]
            }
        }
        
        return {"data": formatted_result}
        
    except Exception as e:
        raise Exception(f"Erro ao buscar status das etapas: {str(e)}") 