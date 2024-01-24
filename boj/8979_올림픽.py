N, K = map(int,input().split()) # N : 전체 국가 수 K : 내가 알고 싶은 국가
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)


for i in range(N):
    if data[i][0] == K:
        score = i

for i in range(N):
    if data[score][1:] == data[i][1:]:
        print(i+1)
        break