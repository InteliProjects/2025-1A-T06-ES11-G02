from config.connection import DatabaseConnection


async def get_falhas_veiculos():
    db = DatabaseConnection()
    query = """
    SELECT *
    FROM vw_contagem_total_erros_veiculo
    ORDER BY contagem_total_erros DESC
    LIMIT 4
    """
    result = db.execute_query(query)
    return {"data": result[0]} 
    

async def get_veiculos_falhas():
    db = DatabaseConnection()

    query = """
    SELECT *
    FROM vw_carros_com_falhas_dia
    """
    result = db.execute_query(query)
    return {"data": result[0]} 
    

async def get_tipo_falhas():
    db = DatabaseConnection()

    query = """
    SELECT *
    FROM vw_contagem_tipo_falhas_totais
    LIMIT 10
    """
    result = db.execute_query(query)
    return {"data": result[0]} 



async def get_falhas_dia():
    db = DatabaseConnection()
    query = """
    SELECT *
    FROM vw_contagem_falhas_dia
    """

    query2 = """
        SELECT
        media
        FROM
        vw_media_falhas_dia
    """
    result = db.execute_query(query)
    result2 = db.execute_query(query2)


    return {"media":result2[0],"data": result[0]}



