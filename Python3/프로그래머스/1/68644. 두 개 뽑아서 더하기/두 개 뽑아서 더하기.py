## numbers에서 서로 다른 인덱스에 있는 두개의 수 뽑기
## 뽑은 수 더해서 만들 수 있는 모든 수 -> 오름차순

def solution(numbers):
    answer = []
    n = len(numbers)
    
    # 1. numbers에서 서로 다른 '인덱스'에 있는 두개 의 수 뽑기
    for i in range(n-1):
        for j in range(i+1, n):
            cnt = numbers[i] + numbers[j]
            if cnt not in answer:
                answer.append(cnt)
                
    # 2. 정렬
    answer.sort()
    
    return answer