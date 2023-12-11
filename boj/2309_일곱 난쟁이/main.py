import sys
sys.stdin = open('imput.txt')

arr = [] # [20, 7, 23, 19, 10, 15, 25, 8, 13]
for _ in range(9):
    a = int(input())
    arr.append(a)

# 전체 sum 을 구한 뒤, sum - 100 인 값 구하기?
# 답이 여러개일 수 있음 !
val = sum(arr) - 100

res = []
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == val:
            res.append(i)
            res.append(j)
# print(res) # 5.6 # 합이 val이 되는 arr의 인덱스

arr[res[0]] = 0
arr[res[1]] = 0

result = []
for i in range(len(arr)):
    if arr[i] > 0:
        result.append(arr[i])

result.sort()
for i in result:
    print(i)