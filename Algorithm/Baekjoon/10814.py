N = int(input())
li = ['0'] * 201

for _ in range(N):
    a, b = input().split()
    li[int(a)] += ' ' + b
    
for idx, i in enumerate(li):
    if i != '0':
        i = list(i.split())
        for j in i[1:]:
            print(idx, j)