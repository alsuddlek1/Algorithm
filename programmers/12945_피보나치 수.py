def solution(n):
    answer = 0
    cnt = 0
    if n < 2:
        cnt = n
    else:
        fib = [0] * (n+1)
        fib[0], fib[1] = 0, 1
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
            cnt = fib[n]

    answer = cnt % 1234567
    return answer