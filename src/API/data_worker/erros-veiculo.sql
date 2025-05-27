CREATE OR REPLACE VIEW vw_contagem_total_erros_veiculo as
SELECT
veiculo.MODELL as modelo
,count(*) as contagem_total_erros
FROM gold_inteli_falhas as falha
LEFT JOIN gold_inteli_veiculo as veiculo ON veiculo.ID = falha.ID
GROUP BY 1
ORDER BY 2 DESC