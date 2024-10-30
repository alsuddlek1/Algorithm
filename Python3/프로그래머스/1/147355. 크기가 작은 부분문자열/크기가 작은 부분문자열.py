## 1. t len(P)만큼 반복문 범위


def solution(t, p):
    answer = 0
    m = len(t)
    n = len(p)
    p_int = int(p)
    
    for i in range(m-n+1):
        t_value = ''
        for j in range(i, i+n):
            t_value += t[j]
        t_int = int(t_value)
        if t_int <= p_int:
            answer += 1
        t_value = ""
        
    return answer










# def solution(t, p):
    
#     answer = 0
#     for i in range(len(t) - len(p) + 1):
#         cnt_str = ""
#         for j in range(i, i + len(p)):
#             cnt_str += t[j]

#         if int(cnt_str) <= int(p):
#             answer += 1
#             cnt_str = ""
                
#     return answer