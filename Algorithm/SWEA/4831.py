T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    cnt = now = next = 0
    while now + K < N:
        next = max([x if x <= now + K else now for x in chargers])
        if next == now:
            print(f'#{tc} 0')
            break
        else:
            now = next
            cnt += 1
    else:
        print(f'#{tc} {cnt}')