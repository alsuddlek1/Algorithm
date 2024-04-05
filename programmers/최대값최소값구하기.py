def solution(s):
    s_list = list(map(int, s.split()))
    
    answer_list = []
    answer_list.append(min(s_list))
    answer_list.append(max(s_list))
    answer = " ".join(map(str, answer_list))

    return answer
