import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = []
ans = [0] * 4
cnt = defaultdict(int)

for i in range(N):
    n = int(input())
    arr.append(n)
    cnt[n] += 1


ans[0] = round(sum(arr) / N)

arr.sort()
ans[1] = arr[N // 2]

cnt_list = []
max_v = max(cnt.values())
for k, v in cnt.items():
    if v == max_v:
        cnt_list.append(k)
        
cnt_list.sort()
ans[2] = cnt_list[0] if len(cnt_list) == 1 else cnt_list[1]

ans[3] = abs(arr[-1] - arr[0])

for i in ans:
    print(i)