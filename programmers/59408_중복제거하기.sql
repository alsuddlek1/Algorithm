-- 중복제거 : DISTINCT
-- 기본 문법
-- SELECT DISTINCT 삭제를 원하는 컬럼 FROM 테이블명; 
-- 여러 컬럼에서 사용하고 싶다면
-- SELECT DISTINCT 삭제를 원하는 컬럼1, 컬럼2 FROM 테이블명; 

SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;