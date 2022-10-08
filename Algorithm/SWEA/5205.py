def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

def partition(l, r):
    p = li[l]
    i, j = l, r

    while i <= j:
        while i <= j and li[i] <= p:
            i += 1
        while i <= j and li[j] >= p:
            j -= 1
        if i < j:
            li[i], li[j] = li[j], li[i]

    li[l], li[j] = li[j], li[l]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    qsort(0, len(li)-1)
    print(f'#{tc}', li[N//2])