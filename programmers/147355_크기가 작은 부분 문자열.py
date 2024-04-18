def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        cnt_str = ""
        for j in range(i, i + len(p)):
            cnt_str += t[j]
        # cnt = int(cnt_str)
        if int(cnt_str) <= int(p):
            answer += 1
            cnt_str = ""

    return answer