n = int(input())

result = 0
i = 0

while result <= n:
    result += i
    if result >= n:
        print(i)
        break
    else:
        i += 1