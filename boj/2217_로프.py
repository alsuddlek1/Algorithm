N = int(input()) # 로프의 개수
rope = [int(input()) for _ in range(N)] # 각 로프의 최대 중량
rope.sort()

cnt = 0
result = 0
for i in range(N):
    cnt = rope[i] * (N-i)
    if cnt >= result:
        result = cnt

print(result)