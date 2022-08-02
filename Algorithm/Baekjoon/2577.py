c = 1

for i in range(3):
    c *= int(input())

for j in range(10):
    print(str(c).count(str(j)))