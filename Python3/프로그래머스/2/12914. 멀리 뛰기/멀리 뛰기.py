## 멀리뛰기를 1칸 or 2칸
## n칸을 멀리 뛰기할 수 있는 경우의 수 % 1234567

# 1. 1칸 -> 1개, 2칸 -> 2개, 3칸 -> 1,1,1 1,2 2,1 3개
# 4칸 -> 1,1,1,1, 1,1,2 1,2,1 2,1,1 2,2 4개
# 5칸 7개
# 1.1.1.1.1
# 1.1.1.2
# 1,2,2
# 1,2,1,1
# 2,1,1,1
# 2,2,1
# 2,1,2
### => f(n) = f(n-1) + f(n-2)


def solution(n):
    memo = [-1] * (n+1)
    
    for i in range(1, n+1):
        if i < 3:
            memo[i] = i
        else:
            memo[i] = memo[i-1] + memo[i-2]

    answer = memo[n] % 1234567
    
    return answer










# def solution(n):
#     cnt = 0
#     if n < 3:
#         cnt = n
#     else:
#         fib = [0] * (n+1)
#         fib[1], fib[2] = 1,2
#         for i in range(3, n+1):
#             fib[i] = fib[i-1] + fib[i-2]
#             cnt = fib[n]
#     answer = cnt % 1234567
#     return answer