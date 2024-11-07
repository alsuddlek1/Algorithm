def solution(arr1, arr2):
    M = len(arr1) # 3
    K = len(arr2) # 2
    N = len(arr2[0]) # 2
        
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1)) ]

    for m in range(M):
        for n in range(N):
            for k in range(K):
                answer[m][n] += arr1[m][k] * arr2[k][n]
    return answer
