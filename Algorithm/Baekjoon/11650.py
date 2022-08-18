from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

dict = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    dict[a].append(b)
    
dict = sorted(dict.items())

for i in dict:
    i[1].sort()
    for j in i[1]:
        print(i[0], j)