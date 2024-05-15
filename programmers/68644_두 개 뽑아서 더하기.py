def solution(numbers):
    answer = []
    n = len(numbers)  # 5

    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            c = numbers[i] + numbers[j]
            if c not in answer:
                answer.append(c)

    answer.sort()

    return answer