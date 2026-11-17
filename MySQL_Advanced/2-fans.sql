-- Ranks country origins of bands by their total (non-unique) fan count
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
