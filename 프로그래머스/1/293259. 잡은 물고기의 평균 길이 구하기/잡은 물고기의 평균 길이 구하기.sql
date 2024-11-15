SELECT ROUND(AVG(CASE WHEN LENGTH IS NULL THEN 10
                       WHEN LENGTH > 10 THEN LENGTH
                       END),2) AS AVERAGE_LENGTH
FROM FISH_INFO