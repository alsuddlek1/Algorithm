import sys
sys.stdin = open('input.txt')

T = int(input()) # 단어 개수

result = 0 # 그룹단어의 개수
for tc in range(1, T+1):
    data = input()
    res = 0
    for i in range(len(data)-1):
        # print(i)
        if data[i] != data[i+1]:
            cnt = data[i+1:]
            if cnt.count(data[i]) > 0:
                res += 1
    if res == 0:
        result += 1
print(result)
