import sys
input = lambda: sys.stdin.readline().strip()

stack = [0] * 10001
top = -1

N = int(input())
for _ in range(N):
    a = input()
    
    if a[:4] == 'push':
        b, c = a.split()
        top += 1
        stack[top] = c
    elif a == 'pop':
        if top == -1: print(-1)
        else:
            print(stack[top])
            top -= 1
    elif a == 'size':
        print(top+1)
    elif a == 'empty':
        if top == -1: print(1)
        else: print(0)
    elif a == 'top':
        if top == -1: print(-1)
        else: print(stack[top])