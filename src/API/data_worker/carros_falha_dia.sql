CREATE OR REPLACE VIEW default.vw_carros_com_falhas_dia
(
    `data` Date,
    `carros_com_falhas` UInt64
)
AS SELECT
    DATE(`DATA DETECCAO`) AS data,
    countDistinct(ID) AS carros_com_falhas
FROM default.gold_inteli_falhas
GROUP BY 1
ORDER BY 1 DESC