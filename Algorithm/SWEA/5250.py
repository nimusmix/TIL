import heapqs

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    costs[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            return cost

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            diff = 0
            if 0 <= nx < N and 0 <= ny < N:
                if heights[nx][ny] > heights[x][y]:
                    diff = heights[nx][ny] - heights[x][y]
                cost2 = cost + 1 + diff
                if costs[nx][ny] > cost2:
                    costs[nx][ny] = cost2
                    heapq.heappush(heap, (cost2, nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000000
    costs = [[INF] * N for _ in range(N)]
    print(f'#{tc}', dijkstra())
