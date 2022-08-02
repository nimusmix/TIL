n, x = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    if i < x:
        print(i, end=' ')