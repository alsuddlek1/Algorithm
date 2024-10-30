## 완전탐색?
# 1. 3중반복문? -> i,j,k + -> 0 이면 answer += 1

def solution(number):
    answer = 0
    n = len(number)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer










# def solution(number):
#     N = len(number)
#     ans = []
#     answer = 0
    
#     def back():
#         nonlocal answer
        
#         if len(ans) == 3:
#             sum_cnt = sum(ans)
#             if sum_cnt == 0:
#                 answer += 1
#             return
#         for i in range(N):
#             if i not in ans:
#                 ans.append(i)
#                 back()
#                 ans.pop()
    
#     back()
    
#     return answer