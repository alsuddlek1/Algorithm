import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
   arr = list(map(int, input().split()))
   n = len(arr)
   a = []

   for i in range(1, 1<<n):
       result = 0
       for j in range(n):
           if i & (1<<j):
               result += arr[j]
       a.append(result)

   for i in range(len(a)):
       if a[i] == 0:
           print(1)
   else:
       print(0)