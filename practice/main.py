import sys
sys.stdin = open('input.txt')

# N = int(input())
#
# for i in range(1,N+1):
#     for j in range(N-i):
#         print(' ', end="")
#     for j in range(i):
#         print('*', end="")
#     print()


# N = [int(input()) for _ in range(9)]
# maxV = 0
# idx = 0
# for i in range(9):
#     if N[i] > maxV:
#         maxV = N[i]
#         idx = i+1
# print(maxV, idx)

A = int(input())
B = int(input())
C = int(input())

data = A*B*C
d_list = list(str(data))
# print(d_list)
matrix = [0] * 10
for i in range(10):
    print(d_list.count(str(i)))
