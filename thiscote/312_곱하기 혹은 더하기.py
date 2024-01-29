s = input()
data = []
for i in range(len(s)):
    data.append(int(s[i]))

cnt = data[0]

for i in range(len(data)-1):
    if cnt + data[i+1] >= cnt * data[i+1]:
        cnt = cnt + data[i+1]
    else:
        cnt = cnt * data[i+1]
    print(cnt)

print(cnt)