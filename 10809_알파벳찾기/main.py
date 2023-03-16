import sys
sys.stdin = open('input.txt')

s = list(input()) # 단어
# print(s)

result = [[-1]*28]
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for i in range(len(alp)): # 알파벳 순서대로 순환
    # i : 알파벳 인덱스
    # print(i)
    ex = []
    for j in range(len(s)): # 단어 순환
        # j : 단어 인덱스
        # print(j)
        if alp[i] == s[j]:
            if s[j] not in ex:
                result[i] = j
                ex.append(s[j])
print(result)