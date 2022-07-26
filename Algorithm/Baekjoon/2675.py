t = int(input())

for i in range(t):
    r, s = input().split()
    for j in s:
        print(j * int(r), end='')
    print()