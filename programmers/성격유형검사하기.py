def solution(survey, choices):
    result_dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        if choices[i] < 4:
            result_dic[survey[i][0]] += (choices[i] * 3) % 4
        elif choices[i] > 4:
            result_dic[survey[i][1]] += choices[i] % 4

    result_list = list(result_dic.keys())

    answer = ""
    for i in range(0, len(result_list), 2):
        if result_dic[result_list[i]] > result_dic[result_list[i + 1]]:
            answer += result_list[i]
        elif result_dic[result_list[i]] < result_dic[result_list[i + 1]]:
            answer += result_list[i + 1]
        else:
            answer += min(result_list[i], result_list[i + 1])
    return answer
