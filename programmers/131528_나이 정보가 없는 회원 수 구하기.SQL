-- COUNT(USER_ID) 로 문제를 풀어도 정답이었지만
-- COUNT(*) 로 풀도록 하자
-- 왜냐하면, USER_ID 가 NULL 값일때 함께 제외되어 결과가 나오기 때문!

SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;