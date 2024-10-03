## PATIENT  : 환자정보

## 12세 이하 / 여자  -> 환자이름, 환자번호, 성별코드, 나이, 전화번호 조회
## 전화번호 null -> 'none' 출력
## 나이 기준 내림차순 , 환자이름 오름차순

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, "NONE") AS TLNO FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = "W"

ORDER BY AGE DESC, PT_NAME