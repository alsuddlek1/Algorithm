import sys
sys.stdin = open('input.txt')

### 2884 알람시계

# h, m = map(int,input().split())
#
# if m-45 >= 0:
#     print(h, m-45)
# elif m-45 < 0:
#     if h-1 >= 0:
#         print(h-1, 60-(45-m))
#     else:
#         print(23, 60-(45-m))


# ### 2525 오븐시계
# A, B = map(int, input().split())
# C = int(input())
# if B+C < 60:
#     print(A, B+C)
# elif B+C >= 60:
#     N = (B+C)//60
#     r = (B+C) % 60
#     if A+N <= 23:
#         print(A+N, r)
#     elif A+N == 24:
#         print(0, r)
#     elif A+N > 24:
#         print(A+N-24, r)

### 2480 주사위
A, B, C = map(int,input().split())
if A == B == C:
    print(10000+A*1000)
elif A != B and A != C and B != C:
    print(max(A,B,C)*100)
else:
    if A == B and A != C:
        print(1000+A*100)
    elif A == C and A != B:
        print(1000+A*100)
    elif A != B and B == C:
        print(1000+B*100)