import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 거슬러 주어야 할 금액
    a = N // 50000
    b = (N - a*50000) // 10000
    c = (N - ((a*50000) + (b*10000))) // 5000
    d = (N - ((a*50000) + (b*10000) + (c*5000))) // 1000
    e = (N - ((a*50000) + (b*10000)+(c*5000)+(d*1000))) // 500
    f = (N - ((a * 50000) + (b * 10000) + (c * 5000) + (d * 1000)+(e*500))) // 100
    g = (N - ((a * 50000) + (b * 10000) + (c * 5000) + (d * 1000) + (e * 500)+(f*100))) // 50
    h = (N - ((a * 50000) + (b * 10000) + (c * 5000) + (d * 1000) + (e * 500) + (f * 100)+(g*50))) // 10
    # print(a, b, c, d)

    print(f'#{tc}')
    print(a, b, c, d, e, f, g, h)

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     cnt = 0
#     result = []
#
#     for i in m_list:
#         result.append(N//i)
#         N %= i
#     print(f'#{tc}')
#     print(*result)