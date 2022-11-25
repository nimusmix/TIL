from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())
ans = deque()

for _ in range(N):
    command = input().split()
    
    if command[0] == 'push_front':
        ans.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        ans.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(ans.popleft() if ans else -1)
    elif command[0] == 'pop_back':
        print(ans.pop() if ans else -1)
    elif command[0] == 'size':
        print(len(ans))
    elif command[0] == 'empty':
        print(0 if ans else 1)
    elif command[0] == 'front':
        print(ans[0] if ans else -1)
    elif command[0] == 'back':
        print(ans[-1] if ans else -1)