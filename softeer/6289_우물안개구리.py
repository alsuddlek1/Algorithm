import sys
input = sys.stdin.readline

N, M = map(int, input().split())
members = list(map(int, input().split()))

# 최고 판단 리스트 (1이면 최고)
cnt_list = [1] * N

for i in range(M):
    # f, s : 비교할 인덱스 + 1
    f, s = map(int, input().split())

    if members[f-1] < members[s-1]:
        cnt_list[f-1] = 0
    elif members[f-1] > members[s-1]:
        cnt_list[s-1] = 0
    elif members[f-1] == members[s-1]:
        cnt_list[f-1] = 0
        cnt_list[s-1] = 0

print(cnt_list.count(1))