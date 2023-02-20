import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# M개의 피자 치즈가 녹아 0이 되면 화덕에서 꺼냄 -> 그 자리에 남은 피자
# 가장 마지막까지 남아있는 피자 번호

# 1. arr 만들기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N : 화덕 크기, M : 피자개수
    arr = list(map(int, input().split()))

# 2. N개의 피자를 화덕에 넣기 : 123 234 345 ,,
    g = arr[:N] # 화덕 개수만큼 자르기
    d = arr[N:] # 남은 피자
    # print(g,d)
    a = deque(g)
    # print(a)

# 3. 왼쪽값 제거 후 오른쪽에 값(새 피자) 추가
    for i in range(len(d)):
        if a[0] == 0: # 0번째 인덱스(1번화덕)이 0이면 삭제(꺼내기)
            a.remove()
            a.appendleft(d[i]) # 꺼낸 후 그 자리에 새 피자 넣기
        else:
            # 아니면 다시 돌려야하는데 드르렁 아오 귀찮아
    # print(a)

# 4.


