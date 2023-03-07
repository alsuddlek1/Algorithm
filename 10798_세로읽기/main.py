import sys
sys.stdin = open('input.txt')

data = [list(input()) for _ in range(5)]

arr = []
for i in range(15): # 문자열 최대 길이가 15
    for j in range(5): # 문자열 다섯개
        if i < len(data[j]):
            arr.append(data[j][i])
print(''.join(arr))