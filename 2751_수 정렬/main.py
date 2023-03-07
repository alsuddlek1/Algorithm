import sys
sys.stdin = open('input.txt')

N = int(input())
data = [int(input()) for _ in range(N)]
# print(data)

data.sort()
# print(data)
for i in data:
    print(i)