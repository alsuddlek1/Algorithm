-- CASE문을 사용한 조건부 논리 적용
-- 'CASE'는 일종의 조건문으로 IF-ELSE 구문과 유사하게 작동
-- 사용법 : CASE-WHEN-THEN-ELSE
-- WHEN은 조건을 지정하며, 조건이 TRUE 일때 THEN 이후의 값 반환
-- ELSE는 조건에 맞지 않을 때 반환할 값
-- END로 CASE 문 종료

SELECT ANIMAL_TYPE,
        CASE
            WHEN NAME IS NULL THEN 'No name'
            ELSE NAME
        END AS NAME, -- 별칭 지정
        SEX_UPON_INTAKE
FROM ANIMAL_INS;