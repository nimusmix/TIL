X = int(input())
target = int(input())

snail = [[0]*X for _ in range(X)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x = y = dr = 0
cnt = X*X

snail[x][y] = cnt

while cnt > 1:
    nx = x + dx[dr]
    ny = y + dy[dr]
    if 0 <= nx < X and 0 <= ny < X and snail[nx][ny] == 0:
        x, y = nx, ny
        cnt -= 1
        snail[x][y] = cnt
    else:
        dr = (dr+1) % 4

li = []
for jdx, j in enumerate(snail):
    print(*j)
    if target in j:
        li.append(jdx+1)
        li.append(j.index(target)+1)
print(*li)