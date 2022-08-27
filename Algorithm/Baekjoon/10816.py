import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
my_cards = list(map(int, input().split()))

c_li = [0] * 20000001

for i in cards:
    c_li[i] += 1
    
for j in my_cards:
    print(c_li[j], end=' ')