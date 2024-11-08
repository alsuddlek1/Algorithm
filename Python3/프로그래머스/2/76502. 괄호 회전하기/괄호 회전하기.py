## 1. s -> 올바른 괄호 판단
# 1-1. stack = [] -> "()" or "[]" or "{}" -> pop
# 1-2. 반복문 다 돌았을 때 len(stack) == 0: cnt += 1

## 2. 칸 이동
# 2-1. s_list = [0] * len(s)
# 2-2. s[1] ~ s[n] -> s_list

## 3. 괄호 판단 반복

def judge(s):
    stack = []
    
    first_par = ["(", "[", "{"]
    second_par = [")", "]", "}"]
    
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2:
            for j in range(3):
                if stack[-2] == first_par[j] and stack[-1] == second_par[j]:
                    stack.pop()
                    stack.pop()
                    break
    return len(stack) == 0
            
            
def solution(s):
    cnt = 0
    n = len(s)
    
    for k in range(n):
        rotated_s = s[k:] + s[:k]
        if judge(rotated_s):
            cnt += 1
    
    return cnt