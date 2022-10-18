import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution():
    body = deque()
    now = 0

    body.append((0, 0, 0))
    snake[0][0] = 1

    while 1:
        i, j, s = body[-1]

        if route[s] == 'L':
            now = (now - 1) % 4
        elif route[s] == 'D':
            now = (now + 1) % 4

        di, dj = direction[now]
        ni, nj = i+di, j+dj

        if 0 <= ni < N and 0 <= nj < N and snake[ni][nj] == 0:
            body.append((ni, nj, s+1))
            snake[ni][nj] = 1
            
            if board[ni][nj] != 0:
                board[ni][nj] = 0
            else:
                ti, tj, _ = body.popleft()
                snake[ti][tj] = 0 
        else:
            return s


N = int(input())
board = [[0]*N for _ in range(N)]                           # 보드
snake = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1                                     # 사과 위치 표시

L = int(input())
route = ['' for _ in range(10001)]
for _ in range(L):
    X, C = input().split()
    route[int(X)] = C                                       # 이동 정보 저장

print(solution()+1)