def solution(arr, K, result):
    print(arr)
    if result != 10:
        return

    for i in range(1,K+1):
        if arr[i]:
            print(data[i], end=' ')
    print()


def make_ncandidates(arr, k, N, c):
    c[0] = True     #
    c[0] = False
    return 2

def backtracking(arr, K, N, result):
    global count
    if result > 10:
        return
    count += 1
    # 종합계산은 result로 진행
    # 후보군 목록
    c = [0] * 2 # 부분 집합 원소 쓸래/말래 만 구분

    # 언제까지 조사 할거야?
    # 현재 조사하는 위치가 최대 조사 상황에 도달할때까지
    if K == N:
        solution(arr, K, result) # 값을 도출하는 함수 실행
    else:
        # 아직 사용해야 하는 원소들이 남았다면
        # 사용할 원소 인덱스 1 증가
        K == 1
        # 내가 해당 원소를 쓸 / 말을 결정하는 경우의 수 2개
        # 배열, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록 배열
        ncandidates = make_ncandidates()
        for i in range(ncandidates): # 후보군 수 만큼 반복
            arr[K] = c[i]
            if arr[K]:
                backtracking(arr, K, N, result + data[N])
            else:
                backtracking(arr, K, N, result)



MAXCANDIDATES = 12
NMAX = 12

count = 0
data = list(range(11))
arr = [0]*NMAX

# 조사를 시작
# 체크할 배열, 시작점,
