import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())    # 건물의 개수
    data = list(map(int,input().split()))   # 건물들의 높이
