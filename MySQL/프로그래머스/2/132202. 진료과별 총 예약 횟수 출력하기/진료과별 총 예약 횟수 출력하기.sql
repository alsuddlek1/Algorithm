# APPOINTMENT : 진료 예약 정보

## 2022년 5월에 예약한 환자수 -> 진료과 코드 별로 조회
# 환자수 오름차순 -> 진료과 오름차순

SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
# SELECT *
FROM APPOINTMENT
WHERE APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD