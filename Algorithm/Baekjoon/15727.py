# 내가 푼 코드
d = int(input())
t = 0
m = 0

for i in range(5, 0, -1):
    if i == 5:
        t += d // 5
        m = d % 5
    else:
        t += m // i
        m %= i
        
print(t)

# 좋은 코드
print((int(input()) + 4)// 5)