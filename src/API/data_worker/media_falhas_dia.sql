CREATE OR REPLACE VIEW vw_media_falhas_dia as
with contagem_dias as (
SELECT
COUNT(DISTINCT date("DATA DETECCAO")) as contagem_data
FROM
gold_inteli_falhas
)
, contagem_falhas as (
SELECT
COUNT(*) as contagem_total
FROM
gold_inteli_falhas
)
SELECT
round((SELECT contagem_total from contagem_falhas)  / (SELECT contagem_data from contagem_dias),2) as media