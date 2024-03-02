def f(i, k):
    if i == k:  # 목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

A = [i for i in range(1,4)]
B = [0] * 3

f(0, 3)
# 1000번 넘어갈 수 없음!
# A = [i for i in range(1000)]
# B = [0] * 1000
#
# f(0, 1000)