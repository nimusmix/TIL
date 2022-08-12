import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 10001

for _ in range(n):
    li[int(input())] += 1
    
for idx, i in enumerate(li):
    if i != 0:
        for _ in range(i):
            print(idx)