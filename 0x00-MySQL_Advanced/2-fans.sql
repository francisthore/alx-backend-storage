-- Ranks country of origins of bands
-- Ordered by number of fans

SELECT DISTINCT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
