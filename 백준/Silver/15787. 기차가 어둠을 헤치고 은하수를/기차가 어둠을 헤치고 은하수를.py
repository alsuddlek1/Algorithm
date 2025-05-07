##### 비트마스킹 + 구현

# 0. 변수 설정
N, M = map(int, input().split())
trains = [0] * (N + 1)  # 1번 -> N번 기차 : 각 기차의 상태를 비트로 표현

for _ in range(M):
    cmd = list(map(int, input().split())) # 좌석
    op = cmd[0]
    i = cmd[1] # 기차 번호

    # op == 1 : i번 기차의 x번 좌석에 사람을 태움
    if op == 1:
        x = cmd[2]
        trains[i] |= (1 << (x - 1))
        
    # op == 2 : i번 기차의 x번 좌석에서 사람이 내림
    elif op == 2: 
        x = cmd[2]
        trains[i] &= ~(1 << (x - 1))
        
    # op == 3 : i번 치가 승객 한칸 뒤로 이동
    elif op == 3:
        trains[i] = (trains[i] << 1) & ((1 << 20) - 1)
        
    # op == 4 ; i번 기차 승객 앞으로 한 칸 이동
    elif op == 4:
        trains[i] >>= 1

# 2. 중복 없는 기차 상태 계산
train_set = set(trains[1:])
print(len(train_set))