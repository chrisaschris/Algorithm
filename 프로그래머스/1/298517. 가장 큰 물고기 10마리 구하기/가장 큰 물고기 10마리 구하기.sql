SELECT ID, 
        CASE
            WHEN LENGTH IS NULL THEN 10
            ELSE LENGTH
        END AS LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC
LIMIT 10