data = input()

count_0 = 0
count_1 = 0

if data[0] == "1": # 전부 0으로 바꾸기
    count_0 += 1
else: # 전부 1로 바꾸기
    count_1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == "1":
            count_0 += 1
        else:
            count_1 += 1

print(min(count_0, count_1))