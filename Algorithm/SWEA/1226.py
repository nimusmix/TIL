def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        if maze[i][j] == 3:
            return 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

for tc in range(1, 11):
    _ = input()
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc} {bfs(sti, stj, N)}')