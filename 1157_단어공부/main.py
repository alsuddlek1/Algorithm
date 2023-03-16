import sys
sys.stdin = open('input.txt')

arr = input().upper()
arrr = list(set(arr)) # M P S I
# print(arrr)

res = [0]*(len(arrr)) # 같은 값 카운트 해줄 1차원 배열
for i in range(len(arrr)):
    for j in arr:
        if arrr[i] == j:
            res[i] += 1
# print(res)
maxV = 0
max_cnt = 0
idx = 0
for x in range(len(res)):
    if maxV <= res[x]:
        maxV = res[x]
        idx = x
# print(maxV, max_cnt, idx)
for y in range(len(res)):
    if res[y] == maxV:
        max_cnt += 1

if max_cnt == 1:
    print(arrr[idx])
elif max_cnt > 1:
    print('?')