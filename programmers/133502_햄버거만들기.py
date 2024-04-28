def solution(ingredient):
    answer = 0
    ham = [1, 2, 3, 1]
    result = []
    
    for i in range(len(ingredient)):
        result.append(ingredient[i])
        if result[-4:] == ham:
            answer += 1
            # for i in range(4):
            #     result.pop()
            del result[-4:]
    
    return answer