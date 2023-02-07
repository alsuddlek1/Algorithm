## 이진탐색

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binarySearch(a, N, key): # 이진탐색
    count = 1
    start = 1
    end = N
    while start <= end:
        c = (start + end) // 2 # c는 중간값
        if a[c] == key:
            return count
        elif a[c] > key:
            end = c   # end를 중간값에서 왼쪽으로 한칸 이동
            count += 1
        elif a[c] < key:  # a[middle] < key
            start = c  # 중간값이 key보다 작으면 start를 중간값에서 오쪽으로 한칸 이동
            count += 1

for tc in range(1, T+1):
    # 400 300 350 (전체 쪽수, A,B가 찾을 쪽 번호)
    arr = list(map(int, input().split()))
    # print(arr)
    N = arr[0]
    A = arr[1]
    B = arr[2]
    a = [i for i in range(N + 1)]
    # print(binarySearch(a, N,A))
    # print(binarySearch(a,N,B))
    if binarySearch(a, N,A) > binarySearch(a,N,B):
        print(f'#{tc} B')
    elif binarySearch(a,N,A) < binarySearch(a,N,B):
        print(f'#{tc} A')
    elif binarySearch(a,N,A) == binarySearch(a,N,B):
        print(f'#{tc} 0')