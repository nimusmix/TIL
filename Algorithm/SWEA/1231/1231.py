import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n:
        inorder(c1[n])
        print(key[n], end='')
        inorder(c2[n])

for tc in range(1, 11):
    N = int(input())
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    key = ['z'] * (N+1)
    
    for _ in range(N):
        arr = list(input().split())
        key[int(arr[0])] = arr[1]
        if len(arr) > 2: c1[int(arr[0])] = int(arr[2])
        if len(arr) > 3: c2[int(arr[0])] = int(arr[3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()