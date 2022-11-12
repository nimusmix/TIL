from collections import deque

N, K = map(int, input().split())
people = deque(range(1, N+1))
ans = []

while people:
    people.rotate(-K+1)
    ans.append(people.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>')