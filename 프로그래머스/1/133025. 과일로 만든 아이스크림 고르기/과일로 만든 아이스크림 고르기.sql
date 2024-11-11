SELECT FH.FLAVOR AS FLAVOR
FROM FIRST_HALF AS FH JOIN ICECREAM_INFO AS II ON FH.FLAVOR = II.FLAVOR
WHERE FH.TOTAL_ORDER > 3000 AND II.INGREDIENT_TYPE LIKE 'FRUIT_BASED'
ORDER BY FH.TOTAL_ORDER DESC