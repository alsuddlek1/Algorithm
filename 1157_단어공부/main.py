import sys
sys.stdin = open('input.txt')

arr = input().upper()
arrr = list(set(arr))
# print(arrr)
a = []
for i in len(arr):
    for j in len(arrr):
        if arr[i] == arrr[j]:
            a.append(arr[i])
print(a)