## FIRST_HALF  : 아이스크림 상반기 주문 정보

## 아이스크림의 맛을 총 주문량 기준 내림차순 -> 출하번호 오름차순

SELECT FLAVOR FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID