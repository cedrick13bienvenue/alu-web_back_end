-- Lists Glam rock bands ranked by their longevity (formed to split, in years)
SELECT band_name, (IF(split = 0, YEAR(CURDATE()), split) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
