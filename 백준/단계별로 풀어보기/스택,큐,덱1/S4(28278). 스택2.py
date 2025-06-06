import sys

input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    command = input().strip()
    if len(command) != 1:
        a, b = map(int, command.split())
    else:
        a = int(command)
       
    if a == 1:
        stack.append(b)
    elif a == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(stack))
    elif a == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)