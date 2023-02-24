import sys
sys.stdin = open('sample_input.txt')

# 몇번 충전?

# 정류장 배열 만들기
T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # K : 한 번 충전할때마다 갈수있는 거리
    # N : 버스 종점 인덱스
    # M : 충전기가 있는 정류장 개수
    st = list(map(int, input().split()))
    # 충전기가 있는 정류장 인덱스가 담긴 리스트
    # 1차원 배열을 만들어서 값이 0이면 충전소 X 1이면 충전소 O
    # 위에 1차원 배열은 어떤 1차원 배열임?
    # 정류장을 만들어 줄건데 0이 (N+1)개인 리스트를 만듦
    station = [0] * (N+1)
    # 충전기가 있는 인덱스에 st 리스트 이용해서 1 표시
    for i in st:
        # i 에 st의 원소 들어가야 station[i]에 1을 넣어서 충전기 위치를 station에 넣을 수 있음
        station[i] = 1
        # print(i) # 1 3 5 7 9
    # 정류장 배열에 st의 원소를 인덱스로 만들어서 값을 1로 변경해줌
    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] <= 1이 있는 곳이 충전기 있는 곳

    # 목표 : 버스가 종점(N)에 도착 bus == N
    bus = 0 # 버스는 0에서 출발해서 N까지 이동 # 버스가 있는 위치
    # bus는 3씩 움직이고 간곳이 1이라면 계속 진행
    bus += 3
    if station[bus] == 1:
        bus += 3
    else:
        bus -= 1


    # 0 이라면 1이 있는 곳까지 뒤로감
    # 다시 1을 만나면 bus는 다시 3씩 이동하고




















# # 정류장 배열
#     station = [0] * (N+1)
#     for i in st:
#         station[i] += 1
#     print(station)
#
# # k만큼 갔다가 뒤로 가장 가까운 정류장으로 돌아가기
#     while :
