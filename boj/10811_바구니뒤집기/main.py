import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
bas = [i for i in range(1, N + 1)]  # 1부터 N 번 까지의 바구니
# print(bas)
# result = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())

    # a 까지는 그대로, a~b 는 역순, b 이후는 그대로
    bas = bas[0:a-1] + bas[a-1:b][::-1] + bas[b:]

print(*bas)












# result = []
    # for i in range(a-1):
        # result.append(bas[i])
    # print(result) # bas[0] / 1
    # for j in range(b-1,a,-1):
        # print(j)