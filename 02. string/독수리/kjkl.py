pattern = 'is'
target = 'This is a book'
p_idx = 0
t_idx = 0
cnt = 0
while t_idx < len(target):
    if target[t_idx] != pattern[p_idx]:
        t_idx = t_idx - p_idx
        p_idx = -1
    p_idx += 1
    t_idx += 1

    if p_idx == len(pattern):
        cnt += 1
        p_idx = 0
print(cnt)