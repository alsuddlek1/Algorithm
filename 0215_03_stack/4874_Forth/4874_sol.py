import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    cal = input().split()
    del cal[-1]
    # print(cal)
    stack = []  # 연산자들을 담아둘 stack
    result = 0  # 최종 결과값

    try:
        for char in cal:
            if char not in '+-*/':
                stack.append(char)
            else:
                x = int(stack.pop())
                y = int(stack.pop())

                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
        # print(stack)
        if len(stack) == 1:
            result = stack.pop()
        else:
            result = 'error'
    except:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {result}')