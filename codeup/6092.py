n = int(input())
data = list(map(int, input().split()))

matrix = [0] * 23

for i in range(n):
    matrix[data[i]-1] += 1

## 리스트를 띄어쓰기로 출력

# 방법 1
result = ' '.join(map(str, matrix))
print(result)

# 방법 2
for res in matrix:
    print(res, end=" ")