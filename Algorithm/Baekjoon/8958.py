n = int(input())

for i in range(n):
    sum_score = 0
    t = list(input().split('X'))
    for k in t:
        score = 0
        if k.isalpha() == True:
            for l in range(1, len(k)+1):
                score += l
            sum_score += score
    print(sum_score)