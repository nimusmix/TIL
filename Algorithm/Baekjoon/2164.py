from collections import deque

N = int(input())
ans = deque(range(1, N+1))

for _ in range(N-1):
    ans.popleft()
    ans.rotate(-1)
    
print(ans[-1])