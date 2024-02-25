def binary(a, N, key):
    start = 0
    end = N-1

    cnt = 0

    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            cnt += 1
            return cnt
        elif a[middle] < key:
            start = middle + 1
            cnt += 1
        else:
            end = middle - 1
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))

    total = data[0]
    page_a = data[1]
    page_b = data[2]

    a = [i for i in range(1, total + 1)]

    cnt_a = binary(a, total, page_a)
    cnt_b = binary(a, total, page_b)

    # A, B 횟수 비교
    if cnt_a > cnt_b:
        print(f"#{tc} B")
    elif cnt_a < cnt_b:
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")

# def binary_search(start, end, AB):
#     mid = (start+end)//2
#     if mid == AB:
#         return 1
#     elif mid > AB:
#         return binary_search(start, mid, AB)+1
#     else:
#         return binary_search(mid, end, AB)+1
#
# for T in range(1, TC+1):
#     end, Pa, Pb = list(map(int,input().split()))
#     start = 1
#     A = binary_search(1, end, Pa)
#     B = binary_search(1, end, Pb)
#     print(f"#{T}", end = " ")
#     if A < B:
#         print("A")
#     elif A > B:
#         print("B")
#     else:
#         print(0)