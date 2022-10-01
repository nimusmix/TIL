# Algorithm_12_0921

## ✨ 반복과 재귀

- 반복을 이용한 선택정렬

  ```python
  def selectionsort(A):
      n = len(A)
      for i in range(n-1):
          minI = i
          for j in range(i+1, n):
              if A[j] < A[minI]:
                  minI = j
          A[minI], A[i] = A[i], A[minI]
  ```

- 재귀를 이용한 선택정렬

  ```python
  def selcetionsort(A, s):
      n = len(A)
      if s == n-1:
          return
      minI = s
      for i in range(s, n):
          if A[minI] > A[i]:
              minI = i
      A[s], A[minI] = A[minI], A[s]
      selectionsort(A, s+1)

<br/>

## ✨ 순열

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- <sub>n</sub>P<sub>r</sub> = n * (n-1) * (n-2) * .. * (n-r+1)

- 재귀 호출을 이용한 순열 생성 *(최소 변경을 통한 방법)*

  ```python
  # p = 데이터가 저장된 배열
  # n = 선택된 원소의 수, k = 원소의 개수
  def perm(n, k):
      if n == k:
          print(p)
      else:
          for i in range(n, k):
              p[n], p[i] = p[i], p[n]
              perm(n+1, k)
      		p[n], p[i] = p[i], p[n]
  ```

  ```python
  # p = 순열을 저장하는 배열, arr = 순열을 만드는 데 사용할 숫자 배열
  # n = 선택된 원소의 수, k = 원소의 개수, used = 사용 여부
  def perm(n, k):
      if n == k:
          print(p)
      else:
          for i in (k-1):
              if not used[i]:
                  p[n] = arr[i]
                  used[i] = 1
                  perm(n+1, k)
                  used[i] = 0
  ```

<br/>

## ✨ 부분 집합

- 바이너리 카운팅을 이용한 부분 집합 생성 *(사전적 순서)*

  - 원소 수에 해당하는 N개의 비트열을 이용
  - n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  n = len(arr)
  
  for i in range(1<<n):                           # 1<<n = 부분집합의 개수
      for j in range(n):                          # 원소의 수만큼 비트를 비교함.
          if i & (1<<j):                          # i의 j번째 비트가 1이면 j번째 원소 출력
              print(arr[j], end=' ')
      print()
  ```

- 재귀 호출을 이용한 부분 집합 생성

  ```python
  def powerset(i, k):
      if i == k:
          for j in range(k):
              if bit[j]:
                  print(arr[j], end=' ')
          print()
      else:
          bit[i] = 0
          powerset(i+1, k)
          bit[i] = 1
          powerset(i+1, k)
  
  arr = [3, 6, 7, 1, 5, 4]
  n = len(arr)
  bit = [0] * n
  powerset(0, n)
  ```

<br/>

## ✨ 조합

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것

- 재귀 호출을 이용한 조합 생성

  ```python
  # an = n개의 원소를 가지고 있는 배열
  # tr = r개 크기의 배열. 조합이 임시 저장될 배열
  def comb(n, r):
      if r == 0:
          print(tr)
      elif n < r:
          return
      else:
          tr[r-1] = an[n-1]
          comb(n-1, r-1)
          comb(n-1, r)
  ```

  

