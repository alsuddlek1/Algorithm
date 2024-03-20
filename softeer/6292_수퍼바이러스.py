import sys
input = sys.stdin.readline

# 지수를 재귀적으로 나눈다.
def f(x, y): # 증가율, 총 시간
    # 총 시간이 1초라면 x(증가율) 리턴
    if y == 1:
        return x

    # 총 시간이 짝수
    elif y % 2 == 0:
        a = f(x, y / 2)
        return a * a % 1000000007

    # 총 시간이 홀수
    else:
        b = f(x, (y - 1) / 2)
        return b * b * x % 1000000007


k, p, n = map(int, input().split()) # 바이러스 수, 증가율, 총시간
n = 10 * n
result = f(p, n)
result *= k
print(result % 1000000007)