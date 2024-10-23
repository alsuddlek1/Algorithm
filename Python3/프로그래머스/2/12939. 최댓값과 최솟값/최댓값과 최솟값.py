def solution(s):
    answer = ''
    s = s.split()
    s_int = []
    for i in range(len(s)):
        s_int.append(int(s[i]))
    
    max_value = max(s_int)
    min_value = min(s_int)
    max_value, min_value = str(max_value), str(min_value)
    answer += min_value
    answer += " "
    answer += max_value
    
    return answer