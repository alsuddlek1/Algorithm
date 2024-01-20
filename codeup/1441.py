def Bubblesort(data, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

N = int(input())

for _ in range(N):
    data = list(map(int, input().split()))
    Bubblesort(data, N)
    print(data)