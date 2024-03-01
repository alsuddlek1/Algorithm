import sys
input = sys.stdin.readline

N = int(input())
stack_list = []

for i in range(N):
    data = input().split()
    # command = data[0]

    if data[0] == "push":
        # num = data[1]
        stack_list.append(data[1])
    elif data[0] == "pop":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop()
    elif data[0] == "size":
        print(len(stack_list))
    elif data[0] == "empty":
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == "top":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])

