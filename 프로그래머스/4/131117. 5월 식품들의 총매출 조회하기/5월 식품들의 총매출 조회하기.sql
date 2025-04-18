SELECT FP.PRODUCT_ID, FP.PRODUCT_NAME, (FP.PRICE*SUM(FO.AMOUNT)) AS TOTAL_SALES
FROM FOOD_PRODUCT AS FP JOIN FOOD_ORDER AS FO ON FP.PRODUCT_ID = FO.PRODUCT_ID
WHERE YEAR(FO.PRODUCE_DATE)=2022 AND MONTH(FO.PRODUCE_DATE)=5
GROUP BY FP.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC