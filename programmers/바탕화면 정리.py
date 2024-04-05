def solution(wallpaper):
    # 바탕화면의 행,열 좌표를 담을 리스트
    row = []
    col = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            # 파일이 있을 경우(#) 행,열 좌표 담아주기
            if wallpaper[i][j] == "#":
                row.append(i)
                col.append(j)
    # 최소값 => 드래그의 시작점
    # 최대값 => 드래그의 끝나는 점
    answer = [min(row), min(col), max(row) + 1, max(col) + 1]
    return answer