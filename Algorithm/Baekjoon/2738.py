n, m = map(int, input().split())
list_a = []
list_b = []

for i in [list_a, list_b]:
    for j in range(n):
        i.append(list(map(int, input().split())))
    
for nc in range(n):
    for mc in range(m):
        list_a[nc][mc] += list_b[nc][mc]
    print(*list_a[nc])