## 자신보다 뒤에 있는 숫자 중 자신보다 크면서 가장 가까이에 있는 수를 뒷 큰수

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)

    return answer
