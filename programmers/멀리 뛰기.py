def solution(n):
    cnt = 0
    if n < 3:
        cnt = n
    else:
        fib = [0] * (n+1)
        fib[1], fib[2] = 1,2
        for i in range(3, n+1):
            fib[i] = fib[i-1] + fib[i-2]
            cnt = fib[n]
    answer = cnt % 1234567
    return answer