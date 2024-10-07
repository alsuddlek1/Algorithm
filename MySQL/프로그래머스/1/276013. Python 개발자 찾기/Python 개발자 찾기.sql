## DEVELOPER_INFOS  : 개발자 프로그래밍 스킬정보

## Python -> id, 이메일, 이름, 성
## id 기준 오름차순

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPER_INFOS
WHERE SKILL_1 = "Python" OR SKILL_2 = "Python" OR SKILL_3 = "Python"
ORDER BY ID