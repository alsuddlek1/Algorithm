input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]) - int(ord('a'))+1)
# 시작 위치 row,col => a1 => 1,1

steps = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)] # 제공된 움직일 수 있는 방향

result = 0

for i in range(8):
    nr = row + steps[i][0]
    nc = col + steps[i][1]
    if 1<= nr <= 8 and 1<= nc <= 8:
        result += 1

print(result)