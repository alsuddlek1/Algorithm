T = int(input())
for _ in range(1, T+1):
    tc, N = list(input().split())
    N = int(N)
    data = list(input().split())

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0] * 10
    result = []

    for i in range(10):
        for j in range(N):
            if num_list[i] == data[j]:
                cnt[i] += 1
    # print(cnt)

    for j in range(10):
        # j= 0 ~ 9
        for k in range(cnt[j]):
            # cnt[j] = 700, 716 ,,,
            # k = 700
            result.append(num_list[j])
    print(tc, *result)


