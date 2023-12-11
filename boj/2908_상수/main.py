import sys
sys.stdin = open('input.txt')

A, B = list(input().split())
A = int(A[0:][::-1])
B = int(B[0:][::-1])

if A > B:
    print(A)
else:
    print(B)