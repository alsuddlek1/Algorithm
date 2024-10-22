## 딕셔너리 활용
# 1. dict = {}
# 2-1. tangerine[i] 값이 dict의 key 값에 없다면 key : value 추가
# 2-2. 있다면 해당 key 값에 value += 1
# 3. value 값이 큰 순서대로 k값에서 빼고 answer += 1


def solution(k, tangerine):
    dic = {}
    answer = 0
    
    for i in range(len(tangerine)):
        if tangerine[i] not in dic:
            dic[tangerine[i]] = 1
        else:
            dic[tangerine[i]] += 1
    
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    for j in range(len(sorted_dic)):
        if k > 0:
            k = k - sorted_dic[j][1]
            answer += 1


    return answer