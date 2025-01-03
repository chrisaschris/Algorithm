SELECT UGU.USER_ID AS USER_ID, UGU.NICKNAME AS NICKNAME, SUM(UGB.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS UGB JOIN USED_GOODS_USER AS UGU ON UGB.WRITER_ID = UGU.USER_ID
WHERE UGB.STATUS LIKE 'DONE'
GROUP BY UGB.WRITER_ID
HAVING SUM(PRICE)>=700000
ORDER BY TOTAL_SALES