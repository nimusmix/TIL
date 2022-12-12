import sys
input = lambda: sys.stdin.readline().strip()

def check(i, j):
    global cnt
    cnt1 = cnt2 = 0
    
    for di in range(8):
        ni = i + di
        for dj in range(8):
            nj = j + dj

            if board[ni][nj] != ans1[di][dj]:
                cnt1 += 1
            if board[ni][nj] != ans2[di][dj]:
                cnt2 += 1
    
    cnt = min(cnt, cnt1, cnt2)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

chess1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
chess2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
ans1 = [chess1, chess2] * 4
ans2 = [chess2, chess1] * 4
cnt = 2500

for i in range(0, N-7):
    for j in range(0, M-7):
        check(i, j)

print(cnt)