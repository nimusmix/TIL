T = int(input())
for tc in range(1, T+1):
    N, *battery = map(int, input().split())
    
    dp = [-1] * N
    for i in range(N-1):
        for j in range(1, battery[i]+1):
            if dp[i+j] == -1:
                dp[i+j] = dp[i] + 1
            if i+j == N-1:
                break
    
    print(f'#{tc} {dp[N-1]}')