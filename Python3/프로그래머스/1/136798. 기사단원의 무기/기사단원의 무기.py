## 자신의 번호의 약수 개수에 해당하는 공격력 무기 구매
## 단 limit보다 큰 공격력을 가지면 -> power 구매

# 약수 구하는 법 약수 구하는 법

def solution(number, limit, power):
    answer = 0
    
    # 1. 1~number 각 수 약수 개수 구하기
    measuer = []
    
    # 1-1. 1부터 number 까지 각각 반복
    for i in range(1, number+1):
        # 1-2. i : 약수 구할 수, j : 약수
        measuer_cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                measuer_cnt += 1
                if j != i // j:
                    measuer_cnt += 1
        # 2. 약수 개수 리스트 중 limit 크기 비교
        if measuer_cnt > limit:
            measuer.append(power)
        else:
            measuer.append(measuer_cnt)
            
    # 3. answer
    answer = sum(measuer)
        
    return answer