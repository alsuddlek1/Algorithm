import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    print(word)

    # 최종 결과값
    result = 0
    stack = []
    for char in word:
        # print(char)
        print(stack, char)
        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack: # 스택이 비었는데
                    result = 0
                    # 더이상 조사할 필요 없다.
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
        print(stack, char)

    if stack:
        result = 0


