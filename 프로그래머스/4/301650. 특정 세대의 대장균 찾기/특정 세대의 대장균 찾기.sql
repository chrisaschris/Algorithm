SELECT C.ID AS ID
FROM ECOLI_DATA AS B RIGHT JOIN ECOLI_DATA AS A ON A.ID=B.PARENT_ID
LEFT JOIN ECOLI_DATA AS C ON B.ID=C.PARENT_ID
WHERE C.ID IS NOT NULL AND A.PARENT_ID IS NULL
ORDER BY ID