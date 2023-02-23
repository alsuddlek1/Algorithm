import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    stick = input()

    result = 1
    stack = []
    for st in stick:
        if st == '(' :
            stack.append(st)
        else:
            if st == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 0
                    break
        print(stack)
    if stack:
        result = 0

    print(result)