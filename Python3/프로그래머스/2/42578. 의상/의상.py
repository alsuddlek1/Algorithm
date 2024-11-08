## 종류별로 1개씩 착용
## clothes[i] = [의상, 의상종류]

def solution(clothes):
    answer = 0
    
    # 1. 옷 종류 별로 딕셔너리
    clothes_dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_dic:
            clothes_dic[clothes[i][1]] += 1
        else:
            clothes_dic[clothes[i][1]] = 1
    
    # 2. (value + 1) * len(clothes_dic) -1
    cnt = 1
    for j in clothes_dic.values():
        cnt *= (j+1)
    
    answer = cnt - 1
    
    return answer