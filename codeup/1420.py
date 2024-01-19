N = int(input())
score_list = []
name_list = []
original_score = []

for _ in range(N):
    name, score = input().split()
    score = int(score)
    score_list.append(score)
    original_score.append(score)
    name_list.append(name)

score_list.sort(reverse=True)

for i in range(N):
    if score_list[2] == original_score[i]:
        print(name_list[i])

