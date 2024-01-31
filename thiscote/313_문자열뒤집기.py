pro_data = input()
data = []
for _ in pro_data:
    data.append(int(_))

count_0 = 0
count_1 = 0

if data[0] == 0: # 전부 0으로 바꾸기
    count_1 = 0
else: # 전부 1로 바꾸기
    count_0 = 0

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == 0:
            count_1 += 1
        else:
            count_0 += 1

print(min(count_1, count_0))