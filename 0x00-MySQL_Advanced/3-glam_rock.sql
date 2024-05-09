-- List all bands with 'Glam rock' as their main style
-- ranked by their longevity

SELECT band_name, IF(split, split-formed, 2022-formed) AS lifespan
    FROM metal_bands
    WHERE style like BINARY '%Glam rock%'
    ORDER BY lifespan DESC;
