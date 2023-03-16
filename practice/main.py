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

# A = int(input())
# B = int(input())
# C = int(input())
#
# data = A*B*C
# d_list = list(str(data))
# # print(d_list)
# matrix = [0] * 10
# for i in range(10):
#     print(d_list.count(str(i)))


# A, B = map(int,input().split())
#
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)
#
# arr = input()
# print(f'{arr}??!')

# A = int(543)
# b_year = int(input())
#
# print(b_year - A)

#10430
# A, B, C = map(int, input().split())
# print((A+B) % C)
# print(((A % C)+(B % C)) % C)
# print((A*B) % C)
# print(((A % C)*(B % C)) % C)

# A = int(input())
# B = input()
# # print(A,B)
#
# mul_1 = A * int(list(str(B))[-1])
# mul_2 = A * int(list(str(B))[1])
# mul_3 = A * int(list(str(B))[0])
# print(mul_1)
# print(mul_2)
# print(mul_3)
# print(A * int(B))
#
# A,B,C = map(int,input().split())
# print(A+B+C)

# print('|\_/|')
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

# T = int(input())
# for tc in range(1, T+1):
#     data = input()
#     result = data[0],data[-1]
#     print(''.join(result))

# data = input()
# print(ord(input()))
#
# T = int(input())
# data = list(input())
# # print(data)
# cnt = 0
# for i in data:
#     cnt += int(i)
# print(cnt)

# T = int(input()) # 테스트케이스
# for tc in range(1, T+1):
#     R, S = input().split()
#     # print(R,S)
#     r = int(R)
#
#     result = []
#     for i in range(len(S)):
#         # print(S[i])
#         result.append(S[i]*r)
#     print(''.join(result))

N = int(input())

for i in range(1, N+1):
    for j in range(1, N-i+1):
        print(' ', end="")
    for j in range(N-i+1,N+i):
        print('*', end="")
    # for j in range(N+i, 2*(N-1)):
    #     print(' ', end="")
    print()
for i in range(N+1, 2*N):
    for j in range(1, i-N+1):
        print(' ', end="")
    for j in range(i-N+1,2*N-i+N):
        print('*', end="")
    # for j in range(2*N-i+N, 2*N):
        # print(' ', end="")
    print()
