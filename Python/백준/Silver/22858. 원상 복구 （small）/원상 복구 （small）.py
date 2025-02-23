# 1. 변수 설정
N, K = map(int, input().split())  # N : 카드 개수, K : 셔플할 횟수
S = list(map(int, input().split()))  # S : K번 셔플 후 최종 값들의 결과
D = list(map(int, input().split()))  # D : 셔플 할 조건

# 최종 상태를 현재 상태로 가정
current = S.copy()

# 2. D를 거꾸로 적용하여 초기 상태 찾기
for _ in range(K):
    previous = [0] * N  # 이전 상태 저장할 리스트
    for i in range(N):
        previous[D[i] - 1] = current[i]
    current = previous

# 3. 초기 상태 출력
for i in current:
    print(i, end=" ")