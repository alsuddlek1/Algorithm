import sys
input = sys.stdin.readline

N, C = map(int, input().split())
data = list(map(int, input().split()))

def black(N, C, data):
    for i in range(N):
        print(data[i])
        C = C - data[i]
        print("i", C)
        if C == 0:
            return 1
        # for j in range(i+1, N):
        #     C = C - data[j]
        #     print("j", C)
        #     if C == 0:
        #         return 1
        #     for l in range(j+1, N):
        #         C = C - data[l]
        #         print("l", C)
        #         if C == 0:
        #             return 1
        #
        # return 0

print(black(N, C, data))