import sys
sys.stdin = open('input.txt')

# 자료받기
N = int(input())
data = list(map(int, input().split())) # 최대 100개
matirx = [0] * 100
maxV = 0
minV = 1000

for tc in range(10):
    N = int(input())
    data = list(map(int, input().split()))  # 최대 100개

    for i in range(100):
        if data[i] > maxV:
            maxV = data[i]
        if data[i] < minV:
            minV = data[i]
    print(maxV, minV)

# 제일 높은 수 -1 => 제일 낮은 수 + 1 을 N번 반복
# 반복 후 제일 큰 수 - 제일 작은 수