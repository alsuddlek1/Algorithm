# 파일 확장자별로 정리 -> 종류별로 몇 개씩 있는지
# 확장자들을 사전 순으로 정렬

# 0. 변수설정
n = int(input())
res_dict = {}

for i in range(n):
    name, ext  = input().split(".")
    if ext not in res_dict:
        res_dict[ext] = 1
    else:
        res_dict[ext] += 1

dict = sorted(res_dict.items())
# print(dict)
for i in dict:
    print(i[0], i[1])

