N= int(input())
data = []

for i in range(N):
    pro_data = int(input())
    data.append(pro_data)

result = 0
for i in range(N-2, -1, -1):
    if data[i] >= data[i+1]:
        result += data[i] - data[i+1] + 1
        data[i] = data[i+1] -1
print(result)