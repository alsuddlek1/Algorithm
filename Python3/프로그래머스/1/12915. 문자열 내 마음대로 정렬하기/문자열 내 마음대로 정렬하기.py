def solution(strings, n):
    # answer = []
    
    # 1. strings 의 n번째 글자 기준으로 정렬
    answer = sorted(strings, key = lambda x : (x[n], x))
    # 2. 정렬 후 기본 sort
    
    return answer