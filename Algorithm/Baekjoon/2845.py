a, b = map(int, input().split())
li = list(map(int, input().split()))

for i in li:
    print(i-a*b, end=' ')