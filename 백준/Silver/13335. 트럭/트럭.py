# 0. 변수설정
n, w, l = map(int, input().split()) # 차 대수, 다리 위 최대 차 개수, 다리무게
arr = list(map(int, input().split()))

cross = [0] * w
time = 0

while cross:
    time += 1
    cross.pop(0)
    if arr: # arr에 차가 남아있다면
        if sum(cross) + arr[0] <= l:
            cross.append(arr[0])
            arr.pop(0)
            
        else:
            cross.append(0)

print(time)
