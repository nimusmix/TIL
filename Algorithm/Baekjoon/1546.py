n = int(input())
s = list(map(int, input().split()))
m = max(s)
new = 0

for i in s:
    new += i/m*100
print(new/n)