from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def solution():
    snake = deque()
    now = 'R'

    snake.append((0, 0, 1))
    check[0][0] = 1

    while True:
        i, j, s = snake[-1]

        if route[s] == 'L':
            if now == 'L': now = 'D'
            elif now == 'R': now = 'U'
            elif now == 'U': now = 'L'
            elif now == 'D': now = 'R'
        elif route[s] == 'D':
            if now == 'L': now = 'U'
            elif now == 'R': now = 'D'
            elif now == 'U': now = 'R'
            elif now == 'D': now = 'L'

        di, dj = direction[now]
        ni, nj = i+di, j+dj

        # if ni < 0 or ni >= N or nj < 0 or nj >= N or check[ni][nj] != 0:
        #     return s

        if 0 <= ni < N and 0 <= nj < N and check[ni][nj] == 0:
            snake.append((ni, nj, s+1))
            # print(ni,nj)
            # print(snake)
            check[ni][nj] = 1
            if board[ni][nj] == 0:
                ti, tj, _ = snake.popleft()
                check[ti][tj] = 0

        else:
            return s



N = int(input())
board = [[0]*N for _ in range(N)]                               # 보드
check = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1                                             # 사과 위치 표시

L = int(input())
route = ['' for _ in range(101)]
for _ in range(L):
    X, C = input().split()
    route[int(X)] = C                                           # 이동 정보 저장

# for i in board:
#     print(i)
# print(route)

print(solution()+1)