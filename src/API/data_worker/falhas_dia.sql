create or replace view vw_contagem_falhas_dia as
SELECT
date("DATA DETECCAO")
,count(*)
FROM 
gold_inteli_falhas
GROUP BY 1
ORDER BY 1 DESC