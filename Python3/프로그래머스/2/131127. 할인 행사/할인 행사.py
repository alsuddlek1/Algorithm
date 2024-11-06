## want, number -> 딕셔너리
## for문 돌면서 discount 로 딕셔너리 값  -1

def solution(want, number, discount):
    answer = 0
    answer_list = []
    
    # 1. 원하는 제품 딕셔너리 생성
    # 1-2. 비교 딕셔너리
    want_dic = {}
    dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        dic[want[i]] = 0
    
    # 2. 반복문 -> dicount
    for i in range(len(discount)-10+1):
        for j in range(i, i+10):
            # 2-1. discount 값이 want_dic에 있으면 해당 value -1
            if discount[j] in dic:
                dic[discount[j]] += 1
                
        # 2-2. dic >= want_dic answer => i+1
        cnt = 0
        for k in range(len(want)):
            if dic[want[k]] >= want_dic[want[k]]:
                cnt +=1
                if cnt == len(want):
                    print(cnt)
                    answer += 1
                    print(answer)

        dic = {key : 0 for key in dic}
        
        
    return answer