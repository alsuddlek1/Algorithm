import sys
sys.stdin = open('input.txt')

data = [list(map(int, input().split())) for _ in range(9)]

maxV = 0
idxi = 0
idxj = 0
for i in range(9):
    for j in range(9):
        if data[i][j] >= maxV:
            maxV = data[i][j]
            idxi = i+1
            idxj = j+1

print(f'{maxV}')
print(f'{idxi} {idxj}')