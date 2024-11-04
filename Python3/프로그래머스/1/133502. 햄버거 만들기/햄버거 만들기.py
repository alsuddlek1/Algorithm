# 조리 순서대로 상수의 앞에 아래서부터 위로 쌓이게 됨
# 빵 1 - 야채 2 - 고기 3 - 빵 1


def solution(ingredient):
    answer = 0
    n = len(ingredient)
    hambuger = [1,2,3,1]
    hambuger_making = []
    
    # 1. hambuger_making[:4] == 1231 이 되면 answer +=1, 아니면 계속 append
    for i in range(n):
        hambuger_making.append(ingredient[i])
        if hambuger_making[-4:] == hambuger:
            answer += 1
            for j in range(4):
                hambuger_making.pop()
            
            
    
    return answer














# def solution(ingredient):
#     answer = 0
#     ham = [1, 2, 3, 1]
#     result = []
    
#     for i in range(len(ingredient)):
#         result.append(ingredient[i])
#         if result[-4:] == ham:
#             answer += 1
#             # for i in range(4):
#             #     result.pop()
#             del result[-4:]
    
#     return answer