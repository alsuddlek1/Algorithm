def solution(brown, yellow):
    answer = [0] * 2
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            x = yellow // i
            y = i
            print(x,y)
            if brown == (x*2 + y*2 + 4):
                answer[0], answer[1] = x+2, y+2
    return answer