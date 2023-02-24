import sys
sys.stdin = open('input.txt')

# 가장 많은 카드에 적힌 숫자카드가 몇장? (이때 카드 장수가 같으면 더 큰수 출력)

# 데이터받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))

# 1차원 배열이용
    cards = [0] * 10
    for i in card:
        cards[i] += 1
    # print(cards)

# 출력
    maxV = 0
    maxC = 0
    for j in range(10):
        if maxC <= cards[j]:
            maxC = cards[j]
            maxV = j

    print(f'#{tc} {maxV} {maxC}')