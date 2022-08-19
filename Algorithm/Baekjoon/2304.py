N = int(input())

li = []

for i in range(N):
    li.append(tuple((map(int, input().split()))))
    
li.sort()
print(li)

s_idx = li[0]
e_idx = li[-1]
h_idx = max(li, key=lambda a:a[1])

print(s_idx, h_idx, e_idx)