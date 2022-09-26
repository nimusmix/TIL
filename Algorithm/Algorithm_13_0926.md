# Algorithm_13_0926

## ✨ 병합 정렬 (Merge Sort)

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

- **자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어내는 데에 활용**

- top-down 방식

- 시간 복잡도 : O(n log n)

- **분할 과정**

    ```python
    def merge_sort(li):
        if len(li) == 1:
            return li
        
        left = []
        right = []
        middle = len(li) // 2
        
        for x in li[:middle]:
            left.append(x)
        for x in li[middle:]:
            right.append(x)
            
        merge_sort(left)
        merge_sort(right)
        
        return merge(left, right)                           # 병합 과정
    ```

- **병합 과정**

    ```python
    def merge(left, right):
        result = []
        
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(rigjt.pop(0))
            elif len(left) > 0:
                result.append(left.pop(0))
            elif len(right) > 0:
                result.append(right.pop(0))
        return result
    ```

<br/>

## ✨ 퀵 정렬 (Quick Sort)

- 주어진 배열을 **기준 아이템(pivot item)** 중심으로, 이보다 작은 것은 왼편 큰 편은 오른편에 위치시키는 방식
- 병합 정렬과 달리 각 부분 정렬이 끝난 후 병합 작업이 필요치 않음.

```python
def Qsort(l, r):
    if l < r:
        s = partition(l, r)                                # Hoare or Lomuto
        Qsort(l, s-1)
        Qsort(s+1, r)
        
li = [7, 2, 5, 3, 4, 5]
N = len(li)
Qsort(0, N-1)
print(li)                                                  # [2, 3, 4, 5, 5, 7]
```

- **Hoare-Partition 알고리즘**

    - 아이디어

        1. 피봇보다 큰 값은 오른쪽, 작은 값은 왼쪽 집합에 위치하도록 함.

        2. 피봇을 두 집합의 가운데에 위치시킴.

    - 피봇 선택 : 왼쪽 끝 / 오른쪽 끝 / 임의의 세 개 값 중에 중간 값

    ```python
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
    ```

- **Lomuto partition 알고리즘**

    ```python
    def partition(p, r):
        x = li[r]
        i = p - 1
        
        for j in (p, r):
            if li[j] <= x:
                i += 1
                li[i], li[j] = li[j], li[i]
        
        li[i+1], li[r] = li[r], li[i+1]
        return i + 1
    ```

<br/>

## ✨ 이진 검색 (Binary Search)

```python
def binary(n, key):                                    # n = li의 길이
    low = 0
    high = n - 1
    
    while low <= high:                                 # < 아니고 <= 임에 유의
        mid = (low + high) // 2
        if li[mid] == key:
            return mid
        elif li[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
  
li = [2, 4, 7, 9, 11, 19, 23]
```

<br/>

## ✨ 백트래킹

- DFS와의 차이 : 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (가지치기)

<br/>

## ✨ 부분 집합의 합

```python
def f1(i, k, t):
    global cnt
    cnt += 1
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += A[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, k, t)
        bit[i] = 1
  
        
def f2(i, k, t, s, rs):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s:
        return
    elif t > s + rs:                                   # rs = 남은 원소의 합
        return
    else:
        bit[i] = 0
        f2(i+1, k, t, s, rs-A[i])
        bit[i] = 1
        f2(i+1, k, t, s+A[i], rs-A[i])
        
A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
f1(0, 10, 10)                                          # cnt = 2047
f2(0, 10, 10, 0)                                       # cnt = 349
```

<br/>

## ✨ NQueen

```python
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            for di, dj in [[-1, 0], [-1, -1], [-1, 1]]:
                ni, nj = i+di, j+dj
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    f(i+1, N)
                    visited[ni][nj] = 0
```
