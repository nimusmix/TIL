# 내가 푼 코드
l = []
mx = 0
mx_l = []

for i in range(4):
    l.append(list(map(int, input().split())))

for j in range(4):
    if j == 0:
        mx = l[j][1]
    else:
        mx = mx - l[j][0] + l[j][1]
    mx_l.append(mx)

print(max(mx_l))

# 좋은 코드
total = 0
m = 0
for i in range(4):
    a, b = map(int, input().split())
    total += b-a
    if m < total : m = total
print(m)
    