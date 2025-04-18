WITH RECURSIVE CTE(ID, PARENT_ID, GENERATION) AS
(
    SELECT ID, PARENT_ID, 1 -- initial row
    FROM ECOLI_DATA ED
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT ED.ID, ED.PARENT_ID, CTE.GENERATION + 1
    FROM CTE
    INNER JOIN ECOLI_DATA ED
    ON CTE.ID = ED.PARENT_ID -- 부모 ID를 구함
)

# SELECT COUNT(B.ID), B.LEVEL
SELECT COUNT(A.ID) AS COUNT, A.GENERATION
FROM CTE AS A LEFT JOIN CTE AS B ON A.ID = B.PARENT_ID
WHERE B.PARENT_ID IS NULL
GROUP BY A.GENERATION