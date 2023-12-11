import sys
sys.stdin = open('sample_input.txt')

def aa(i, res):
    global result
    if i > 12:
        result = min(res, result)
        return

    if result <= res:
        return

    aa(i+1, res+day*data[i])
    aa(i+1, res+mon)
    aa(i+3, res+mon3)
    aa(i+12, res+year)

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    result = 1000000000
    aa(1, 0)
    print(result)