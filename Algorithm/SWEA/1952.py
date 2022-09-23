T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12                                                              # dp를 이용하여 최소 가격의 누적합 저장
    month = min(month, month3)                                                 # 3개월 이용권이 1개월 이용권보다 저렴한 경우가 있으므로 비교하여 최소값 저장
    dp[0] = min(plan[0]*day, month)                                            # 일일 이용권 이용 가격과 1개월 이용권 가격 비교

    for j in range(1, 3):                                                      # 3월까지는 이전 달 가격 + 일일 이용권 이용 가격, 이전 달 가격 + 1개월 이용권 가격, 3개월 이용 가격의 최소값 저장
        dp[j] = min(dp[j-1] + min(plan[j]*day, month), month3)
    for j in range(3, 12):
        dp[j] = min(dp[j-1] + min(plan[j]*day, month), dp[j-3] + month3)       # 4월부터는 이전 달 가격 + 일일 이용권 이용 가격, 이전 달 가격 + 1개월 이용권 가격, 3달 전 가격 + 3개월 이용 가격의 최소값 저장

    print(f'#{tc}', min(dp[11], year))                                         # dp 마지막에 저장된 값과 연간 이용권 중 최소값 저장

