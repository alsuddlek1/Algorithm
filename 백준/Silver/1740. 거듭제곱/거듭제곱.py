n = int(input())

res = 0
c = 0

while n > 0:
    if n % 2 == 1:
        res += 3 ** c
    n //= 2
    c += 1

print(res)