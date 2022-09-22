T = int(input())

for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    A = [0] * 12                                           # player1. indexError를 고려하여 12칸 생성
    B = [0] * 12                                           # player2. indexError를 고려하여 12칸 생성
    Acnt = Bcnt = winner = 0

    for i in range(0, 12, 2):
        A[tmp[i]] += 1
        B[tmp[i+1]] += 1

        for j in range(10):                                # 카드를 한 장씩 가져올 때마다 babygin 여부 검사
            if A[j] >= 3:                                  # triplet
                A[j] -= 3
                Acnt += 1
            if A[j] > 0 and A[j+1] > 0 and A[j+2] > 0:     # run
                A[j] -= 1
                A[j+1] -= 1
                A[j+2] -= 1
                Acnt += 1

        if Acnt > Bcnt:
            winner = 1
            break

        for j in range(10):
            if B[j] >= 3:                                  # triplet
                B[j] -= 3
                Bcnt += 1
            if B[j] > 0 and B[j+1] > 0 and B[j+2] > 0:     # run
                B[j] -= 1
                B[j+1] -= 1
                B[j+2] -= 1
                Bcnt += 1

        if Bcnt > Acnt:
            winner = 2
            break

    print(f'#{tc}', winner)