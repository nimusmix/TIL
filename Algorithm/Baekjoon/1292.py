A, B = map(int, input().split())

li = [0] * 10000001
k = 1

for i in range(1, B+1):
    for j in range(i):
        li[k] = i
        k += 1

print(sum(li[A:B+1]))