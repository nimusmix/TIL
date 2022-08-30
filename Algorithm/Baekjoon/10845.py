import sys
input = lambda: sys.stdin.readline().strip()

queue = [0] * 10001
front = -1
rear = -1

N = int(input())
for _ in range(N):
    a = input()
    
    if a[:4] == 'push':
        b, c = a.split()
        rear += 1
        queue[rear] = c
    elif a == 'pop':
        if front == rear: print(-1)
        else:
            front += 1
            print(queue[front])
    elif a == 'size':
        print(rear - front)
    elif a == 'empty':
        if front == rear: print(1)
        else: print(0)
    elif a == 'front':
        if front == rear: print(-1)
        else: print(queue[front+1])
    elif a == 'back':
        if front == rear: print(-1)
        else: print(queue[rear])