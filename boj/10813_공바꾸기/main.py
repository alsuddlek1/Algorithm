import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

bas = []    # 1번부터 N번까지 번호가 있는 바구니
for _ in range(1, N+1):
    bas.append(_)
# print(bas)

for i in range(M):
    x, y = map(int, input().split()) # M번 교환할 바구니의 인덱스
    ex = bas[y-1]           # 임시로 y 바구니 수 담아두고
    bas[y-1] = bas[x-1]     # 위치 교환
    bas[x-1] = ex           # 빈 인덱스에 다시 채워줌
print(*bas)
