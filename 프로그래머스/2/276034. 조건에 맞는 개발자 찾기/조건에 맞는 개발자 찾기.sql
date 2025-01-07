# SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
# FROM DEVELOPERS
# WHERE TRUNC(CONV(SKILL_CODE, 10, 2)/100000000,0) % 10 = 1 
# OR TRUNC(CONV(SKILL_CODE, 10, 2)/10000000000,0) % 10 = 1
# ORDER BY ID

# SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
# FROM DEVELOPERS
# WHERE FLOOR(CONV(SKILL_CODE, 10, 2)/100000000) % 1000 = 1
# OR FLOOR(CONV(SKILL_CODE, 10, 2)/100000000) % 1000 = 100
# OR FLOOR(CONV(SKILL_CODE, 10, 2)/100000000) % 1000 = 101
# ORDER BY ID

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
    OR SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY ID;