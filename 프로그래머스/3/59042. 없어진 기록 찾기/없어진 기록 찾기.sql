SELECT AO.ANIMAL_ID AS ANIMAL_ID, AO.NAME AS NAME
FROM ANIMAL_INS AS AI RIGHT JOIN ANIMAL_OUTS AS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID