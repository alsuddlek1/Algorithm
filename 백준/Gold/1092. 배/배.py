import sys

# 1. 변수설정
n = int(input())
cranes = list(map(int, input().split())) # 각 크레인 무게 제한
m = int(input()) # 박스의 수
boxes = list(map(int, input().split()))
time = 0

# 2. 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 3. 무게 비교 후 시간 측정
# 3-1. boxes의 가장 큰 무게와 가장 큰 크레인
if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()

while len(boxes):
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    time += 1

print(time)