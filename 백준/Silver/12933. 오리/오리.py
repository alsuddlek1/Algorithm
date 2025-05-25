#### 다시 풀기

sound = input().strip()
order = "quack"
status = [0] * 5  # q, u, a, c, k 상태에 있는 오리 수
max_ducks = 0

for ch in sound:
    idx = order.find(ch)
    if idx == -1:
        print(-1)
        exit()

    if idx == 0:
        # 새로운 오리 시작
        status[0] += 1
    else:
        if status[idx - 1] == 0:
            # 이전 상태에 오리가 없으면 잘못된 순서
            print(-1)
            exit()
        status[idx - 1] -= 1
        status[idx] += 1

    # 현재 진행 중인 오리 수 추적
    max_ducks = max(max_ducks, sum(status[:4]))

# 모든 오리가 완전히 "quack"을 끝냈는지 확인
if sum(status[:4]) != 0 or status[4] * 5 != len(sound):
    print(-1)
else:
    print(max_ducks)