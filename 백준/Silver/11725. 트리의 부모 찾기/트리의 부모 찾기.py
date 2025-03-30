from collections import deque

# 1. 변수설정
n = int(input())
arr1 = [[0] for _ in range(n+1)] # 자식
arr2 = [0] * (n+1) # 부모 리스트

for i in range(n-1):
    x, y = map(int, input().split())
    
    # 트리 만들기
    arr1[x].append(y)
    arr1[y].append(x)

arr2[1] = 0
q = deque()
q.append(1)

while q:
    curr = q.popleft()
    for i in arr1[curr]:
        if arr2[i] == 0:
            arr2[i] = curr
            q.append(i)

# 출력
for i in arr2[2:]:
    print(i)