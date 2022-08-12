import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

li.sort()
print(*li, sep='\n')