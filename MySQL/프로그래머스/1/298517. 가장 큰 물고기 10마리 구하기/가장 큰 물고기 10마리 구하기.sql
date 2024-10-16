## FISH_INFO  : 물고기 정보

## 가장 큰 물고기 10마리의 ID, 길이 출력
## 길이 기준 내림차순, ID 오름차순

SELECT ID, LENGTH FROM FISH_INFO
ORDER BY LENGTH DESC, ID
LIMIT 10