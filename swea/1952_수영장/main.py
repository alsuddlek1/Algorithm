import sys
sys.stdin = open('sample_input.txt')


def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n > 12:
        ans = min(ans, sm)
        return

    dfs(n+1, sm+day*lst[n]) # 일간권
    dfs(n+1, sm+mon) # 월권
    dfs(n+3, sm+mon3)   # 분기권
    dfs(n+12, sm+year) # 연간권

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = 365*3000 # 최악의경우(최대값)
    dfs (1, 0)

    print(f'#{tc} {ans}')