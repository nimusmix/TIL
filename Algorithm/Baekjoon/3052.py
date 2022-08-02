# 내가 푼 코드
l = [int(input()) for _ in range(10)]
ll = []

for i in l:
    if (i%42) not in ll:
        ll.append(i%42)

print(len(ll))

# 좋은 코드
b = [int(input())%42 for _ in range(10)]
print(len(set(b)))