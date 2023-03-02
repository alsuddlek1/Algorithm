import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int,input().split())) for _ in range(9)]
    # print(data)

    # 가로 : 1부터 9까지
    Acnt = 0
    for i in range(9):
        A = []
        # i : 스도쿠 행 인덱스
        for j in range(9):
            # j : 스도쿠 열 인덱스
            A.append(data[i][j])
        # print(A)
        AA = set(A)
        # print(AA)
        if len(AA) == 9:
            Acnt += 1

    # 세로 : 1부터 9까지
    Bcnt = 0
    for i in range(9):
        B = []
        # i : 스도쿠 행 인덱스
        for j in range(9):
            # j : 스도쿠 열 인덱스
            B.append(data[j][i])
        # print(A)
        BB = set(B)
        # print(BB)
        if len(BB) == 9:
            Bcnt += 1

    # 3*3 : 1부터 9까지
    Ccnt = 0
    for i in range(0,7,3):
        for j in range(0,7,3):
            C = []
            for k in range(i,i+3):
                for l in range(j, j+3):
                    # print(k,l)
                    C.append(data[k][l])
            # print(C)
            CC = set(C)
            if len(CC) == 9:
                Ccnt += 1

    if Acnt == 9 and Bcnt == 9 and Ccnt == 9:
        print(f'#{tc}', 1)

    else:
        print(f'#{tc}', 0)