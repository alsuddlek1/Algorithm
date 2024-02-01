import sys

N = int(sys.stdin.readline())
s = set()
for _ in range(N):
    data = sys.stdin.readline().strip().split()

    if len(data) == 1:
        if data[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        func, x = data[0], data[1]
        x = int(x)

        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)