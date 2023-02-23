import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    cal = input()
    stack = []
    result = ''
    for char in cal:
        if char in '+-*/':
            if char in '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += char
    while stack:
        result += stack.pop()
    # print(result)

    stacks = []
    results = 0
    for char in result:
        if char not in '+-*/':
            stacks.append(char)
        else:
            x = int(stacks.pop())
            y = int(stacks.pop())
            if char == '+':
                stacks.append(y+x)
            elif char == '-':
                stacks.append(y-x)
            elif char == '*':
                stacks.append(y*x)
            elif char == '/':
                stacks.append(y//x)
    results = stacks.pop()
    print(results)