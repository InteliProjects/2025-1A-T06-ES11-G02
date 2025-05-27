CREATE OR REPLACE VIEW vw_contagem_tipo_falhas_totais as
SELECT
TYPE_ID
, count(*)
FROM
gold_inteli_falhas
GROUP BY 1
ORDER BY 2 DESC