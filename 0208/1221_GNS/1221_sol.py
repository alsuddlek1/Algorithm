## GNS

import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

# 외계인 숫자 체계
numbers = ['ZRO' , 'ONE', 'TWO','THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


for tc in range(1, T+1):
    arr = input().split() # 케이스번호, 케이스 길이
    a = arr[0]
    b = int(arr[1])
    num = list(input().split()) #외계인한테 받은 숫자
    result = []
    for i in range(len(numbers)):
        for j in num:
            if j == numbers[i]:
                result.append(j)

    print(f'{a}')
    print(*result)