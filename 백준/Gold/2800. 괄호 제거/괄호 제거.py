from itertools import combinations

arr = list(input())
stack = []

## 1. 쌍으로 이루어진 괄호 인덱스
par = []
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(i)
    elif arr[i] == ")":
        s = stack.pop()
        par.append((s, i))

## 2. par 부분집합
res = set()
for i in range(1, len(par)+1):
    for comb in combinations(par, i):
        temp = arr[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        res.add("".join(temp))

for i in sorted(list(res)):
    print(i)
