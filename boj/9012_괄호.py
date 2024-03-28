def VPS(N, data_list):
    count_list = [0]*N
    if N % 2 != 0:
        return "NO"
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                if data_list[i] == "(" and data_list[j] == ")" and count_list[j] == 0 and count_list[i] == 0:
                    count_list[i] = 1
                    count_list[j] = 1
                    break
    if count_list.count(1) == N:
        return "YES"
    else:
        return "NO"

T = int(input())

for i in range(T):
    data = input()
    data_list = []
    for _ in data:
        data_list.append(_)
    N = len(data_list)
    print(VPS(N, data_list))