def dijkstra():
    U = [0] * (N+1)
    U[0] = 1
    for i in range(N+1):
        D[i] = adjM[0][i]

    for _ in range(N):
        minV = 99
        w = 0
        for i in range(N+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(N+1):
            if 0 < adjM[w][v] < 99:
                D[v] = min(D[v], D[w]+adjM[w][v])

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[99] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
    D = [0] * (N+1)
    dijkstra()
    print(f'#{tc}', D[N])
