T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    minP = 0
    maxP = N-1
    i = j = 0

    for v in range(1, N*N+1):
        if i == minP and j == minP:
            step = [0, 1]
        elif i == minP and j == maxP:
            step = [1, 0]
        elif i == maxP and j == maxP:
            step = [0, -1]
        elif i == maxP and j == minP:
            step = [-1, 0]

        if snail[i][j] != 0:
            i += 1
            j += 1
            minP += 1
            maxP -= 1

        snail[i][j] = v
        i += step[0]
        j += step[1]

    print(f'#{tc}')
    for k in snail:
        print(*k)