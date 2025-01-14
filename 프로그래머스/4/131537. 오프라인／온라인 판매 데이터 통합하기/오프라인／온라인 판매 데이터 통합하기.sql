# SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, 
#         PRODUCT_ID, 
#         USER_ID, 
#         SALES_AMOUNT
# FROM ONLINE_SALE
# # WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') ='2022-03'
# WHERE YEAR(SALES_DATE)=2022 AND MONTH(SALES_DATE)=3
# UNION ALL
# SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, 
#         PRODUCT_ID, 
#         'NULL' AS USER_ID, 
#         SALES_AMOUNT
# FROM OFFLINE_SALE
# # WHERE DATE_FORMAT(SALES_DATE,'%Y-%m') ='2022-03'
# WHERE YEAR(SALES_DATE)=2022 AND MONTH(SALES_DATE)=3
# ORDER BY SALES_DATE, PRODUCT_ID, USER_ID

SELECT date_format(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE year(SALES_DATE) = 2022 AND month(SALES_DATE) = 3

UNION ALL

SELECT date_format(SALES_DATE,'%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE year(SALES_DATE) = 2022 AND month(SALES_DATE) = 3

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID


