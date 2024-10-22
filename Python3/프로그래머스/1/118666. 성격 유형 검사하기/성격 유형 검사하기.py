## 딕셔너리 활용
# 1. dic = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0,}
# 2-1. data[1] = 1,2,3 -> dic[data[0]] += 1,2,3
# 2-2 data[1] = 4 -> pass
# 2-3 data[1] = 5,6,7 -> dic[data[0]] += 1,2,3
# 3. dic에서 0,1 / 2,3/ 4,5 중 큰 수
# 3-1. 같을 경우 앞에 수

def solution(survey, choices):
    dic = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    answer = ''
    n = len(choices)
    survey_set = [("R", "T"), ("C", "F"), ("J","M"), ("A", "N")]
    
    for i in range(n):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4

    for a,b in survey_set:
        if dic[a] >= dic[b]:
            answer += a
        else:
            answer += b
        
    
    return answer