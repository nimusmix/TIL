o = list(map(int, input().split()))
n = [1, 1, 2, 2, 2, 8]

for i in range(len(o)):
    print(n[i] - o[i])