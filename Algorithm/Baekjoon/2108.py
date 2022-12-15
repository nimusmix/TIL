import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []

for i in range(N):
    n = int(input())
    arr.append(n)


print(round(sum(arr) / N))

arr.sort()
print(arr[N // 2])

cnt = Counter(arr).most_common()
print(cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0])

print(abs(arr[-1] - arr[0]))