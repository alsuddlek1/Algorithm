## 보호소에서 중성화 수술한 동물 정보
# 보호소 들어올 때는 중성화 x
# 나갈때는 중성화 o
# 아이디, 생물종, 이름 조회 -> 아이디 순 조회

SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS
USING(ANIMAL_ID)
WHERE INS.SEX_UPON_INTAKE REGEXP 'Intact' AND
      OUTS.SEX_UPON_OUTCOME REGEXP 'Spayed|Neutered';