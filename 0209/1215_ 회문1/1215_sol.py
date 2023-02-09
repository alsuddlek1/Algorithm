import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(10):
    M = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    for i in range(8):
        for l in range(8-M+1):
            word_list = []
            cnt = 0
            for j in range(l, l + M):
                word_list.append(arr[i][j])  # arr에서 비교하면서 한 문장씩 받아오기
                new_word_list = word_list[:]  # 받아온 리스트를 새 리스트로 받음
                new_word_list.reverse()
            for k in range(len(word_list)):
                if word_list[k] == new_word_list[k]:  # 원래 리스트와 새 리스트의 모양 비교
                    cnt += 1  # 모양이 같을 경우 카운트
            if cnt == M:  # 길이가 M인 회문이므로 카운트와 M이 같을 경우 리스트 반환
                print(f'#{tc}', ''.join(word_list))

            # 전치행렬로 바꾸기
        for i in range(8):
            for j in range(8):
                if i < j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        for i in range(8):  # 세로 회문 비교
            for l in range(8 - M + 1):
                word_list = []
                cnt = 0
                for j in range(l, l + M):
                    word_list.append(arr[i][j])

                    new_word_list = word_list[:]
                    new_word_list.reverse()
                for k in range(len(word_list)):
                    if word_list[k] == new_word_list[k]:
                        cnt += 1
                if cnt == M:
                    print(f'#{tc}', ''.join(word_list))