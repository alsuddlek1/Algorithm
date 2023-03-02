import sys
sys.stdin = open('sample_input.txt')

# 과제를 제출하지 않은 학생 오름차순 출력

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    # N : 전체 학생 수
    # K : 과제 제출한 학생수
    arr = list(map(int, input().split()))
    # arr : 과제 제출한 학생의 번호

    # 1~N에서 arr에 해당하는 번호를 제외하고 출력하고싶은뎅 오또카지
    # 배열만들어서 제출 학생 인덱스에 1넣기 0인 리스트 인덱스 뽑기
    matrix = [0]*(N+1)        # 학생들 넣을 리스트
    # print(matrix)
    for i in arr:
        # i : arr 의 원소
        # print(i)
        matrix[i] = 1
    # print(matrix)
    result = []
    for j in range(1,N+1):
        if matrix[j] == 0:
            result.append(j)
    print(f'#{tc}', *result)