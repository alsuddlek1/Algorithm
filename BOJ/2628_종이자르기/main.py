import sys
sys.stdin = open('input.txt')

l,h = map(int, input().split())
# l : 종이의 가로길이
# h : 종이의 세로길이
N = int(input())    # 칼로 잘라야 하는 점선의 개수
for tc in range(1, N+1):
    line = list(map(int,input()))   # 잘라야할 점선
