import sys
input = sys.stdin.readline

def binary(b, N):
    s = 0
    e = N-1

    while s <= e:
        m = (s+e)//2
        if A[m] == b:
            return 1
        elif A[m] > b:
            e = m-1
        else:
            s = m+1
    return 0

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())

for b in list(map(int, input().split())):
    print(binary(b, N))