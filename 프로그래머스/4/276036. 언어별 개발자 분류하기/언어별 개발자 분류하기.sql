WITH AA AS
(
    SELECT
        CASE
        WHEN SKILL_CODE & (SELECT SUM(CODE)
                            FROM SKILLCODES
                            WHERE CATEGORY = 'FRONT END')
            AND SKILL_CODE & (SELECT CODE
                            FROM SKILLCODES
                            WHERE NAME = 'PYTHON')
        THEN 'A'
        WHEN SKILL_CODE & (SELECT CODE
                            FROM SKILLCODES
                            WHERE NAME = 'C#')
        THEN 'B'
        WHEN SKILL_CODE & (SELECT SUM(CODE)
                            FROM SKILLCODES
                            WHERE CATEGORY = 'FRONT END')
        THEN 'C'
        ELSE NULL
    END AS GRADE, ID, EMAIL
    FROM DEVELOPERS
    WHERE SKILL_CODE & (SELECT SUM(CODE)
            FROM SKILLCODES
            WHERE CATEGORY = 'FRONT END' OR NAME = 'PYTHON' OR NAME = 'C#')
    ORDER BY GRADE, ID
)
SELECT *
FROM AA
WHERE GRADE IS NOT NULL


    
