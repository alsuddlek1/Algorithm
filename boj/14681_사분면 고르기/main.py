import sys
sys.stdin = open('input.txt')

x = int(input())
y = int(input())

# x,y 각 범위를 따져서 출력

if x >= 0 and y >= 0:
    print(1)
elif x >= 0 and y < 0:
    print(4)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y > 0:
    print(2)