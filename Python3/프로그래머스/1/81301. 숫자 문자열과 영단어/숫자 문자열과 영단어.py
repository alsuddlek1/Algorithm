# 영어 -> 숫자로 변환
# 딕셔너리로 영단어, 숫자 저장
# 딕셔너리[영어] 롤 숫자 탐색

def solution(s):
    answer = ""
    num_dic = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, 'eight' : 8, "nine" : 9}
    num_str = ""
    for i in s:
        if (i.isnumeric()):
            answer += i
        else:
            num_str += i
            if num_str in num_dic:
                answer += str(num_dic[num_str])
                num_str = ""
                
    return int(answer)











# def solution(s):
#     num_dic = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, 'eight' : 8, "nine" : 9}
#     answer = ""
#     num_str = ""
    
#     for i in s:
#         if (i.isnumeric()):
#             answer += i
#         else:
#             num_str += i
#             if num_str in num_dic:
#                 answer += str(num_dic[num_str])
#                 num_str = ""
    
    
#     return int(answer)