## 정사각형 격자판
## wallpaper : 바탕화면 상태를 나타낸 문자열 배열
## . : 빈칸, "#" : 파일 있는 칸
## 최소한의 이동거리를 갖는 한번의 드래그를 모든 파일 선택

# !! x,y 작은 좌표와 x,y가 가장 큰 좌표 구하기
# 1. x : 0, 1, 2
# 2. y : 1, 2, 3
# => (0,1), (2+1,3+1)


def solution(wallpaper):
    answer = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    x_list = []
    y_list = []
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                x_list.append(i)
                y_list.append(j)
                
    answer.append(min(x_list))
    answer.append(min(y_list))
    answer.append(max(x_list)+1)
    answer.append(max(y_list)+1)
                

    return answer