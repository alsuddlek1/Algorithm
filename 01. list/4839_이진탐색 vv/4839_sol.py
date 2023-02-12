import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binarySerach(a, N, key):
    start = 1
    end = N
    count = 1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return count
        elif a[middle] > key :
            end = middle
            count += 1
        elif a[middle] < key :
            start = middle
            count += 1
        
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    A_key = arr[1]
    B_key = arr[2]
    a = [i for i in range(N+1)]

    # print(binarySerach(a, N, A_key))

    if binarySerach(a, N, A_key) > binarySerach(a, N, B_key):
        print(f'#{tc} B')
    elif binarySerach(a, N, A_key) < binarySerach(a, N, B_key):
        print(f'#{tc} A')
    elif binarySerach(a, N, A_key) == binarySerach(a, N, B_key):
        print(f'#{tc} 0')

