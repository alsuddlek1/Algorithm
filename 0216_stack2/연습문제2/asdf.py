def powerset(arr, K, result):
    global count
    if sum(result) > 10:
        return
    count += 1

    if K == len(arr):
        if sum(result) == 10:
            print(result)
        return
    powerset(arr, K+1, result + [arr[K]])
    powerset(arr, K+1, result)

arr = list(range(1, 11))

# 원본 배열, 사용한 원소 수, 총합 리스트(사용할 원소 담음)
powerset(arr, 0, [])
