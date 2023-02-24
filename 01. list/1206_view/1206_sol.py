import sys
sys.stdin = open('input.txt')

# 좌우 두칸씩 비어있는 아파트 층수 개수 출력

# input
for tc in range(10):
    N = int(input())  # 건물개수
    data = list(map(int, input().split()))

# 범위 (2, N-2) : 맨 왼쪽, 오른쪽은 건물 x
    result = 0
    for i in range(2, N-2):
        floor = data[i]
        # 좌우 두칸씩 층수 비교
        for j in range(i-2,i+2+1):
            # print(data[j])
            if i == j: # i = j 는 안해도되지않나
                continue
            # 조망권이 있는 아파트 층수 구해야함
            if data[i] > data[j]:
                apt = data[i] - data[j]
                if apt < floor:
                    floor = data[i] - data[j]
            elif data[i] <= data[j]:
                break
        else:
            result += floor
    print(f'#{tc+1} {result}')