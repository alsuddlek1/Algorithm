import sys
sys.stdin = open('input.txt')

asc = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 10, M : 70
    data = [input() for _ in range(N)]

    # dat배열에서 암호코드 정보 추출
    A = ''
    for i in range(N): # 0~9
        for j in range(M-1, -1, -1): # j = 69 부터 0번 인덱스까지 반대로 순회
            if data[i][j] == '1':
                # print(j)
                for k in range(j-55, j+1): # j부터 56자리 숫자
                    if len(A) < 56:
                        A += data[i][k]
    # print(A)
    # 암호코드 7자리씩 슬라이싱
    B = []
    for i in range(0, 56, 7):
        B.append(A[i:i+7])
    # print(B)
    # asc와 비교 후 암호 출력
    C = []
    for i in B:
        C.append(asc[i])
    # print(C)
    # 홀수자리*3 + 짝수자리 == 10의 배수 : 암호
    D = (C[0]+C[2]+C[4]+C[6])*3 + (C[1]+C[3]+C[5]+C[7])
    # print(D)
    if D % 10 == 0:
        result = sum(C)
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')
    # 암호일 경우 각 자리수 합 결과 출력
    # print(f'#{tc} {result}')