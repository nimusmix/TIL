# Algorithm_07_0810

## ✨ 2차원 배열의 접근

- 열 우선 순회

    ```python
    for j in range(M):
      for i in range(N):
        print(arr[i][j])
    ```

- 지그재그 순회

    ```python
    for i in range(N):
      for j in range(M):
        print(arr[i][j + (m-1-2*j) * (i%2)])
    ```

- 델타를 이용한 2차 배열 탐색

    ```python
    di = [0, 0, -1, 1]                    # 상하좌우
    dj = [-1, 1, 0, 0]
    
    for i in range(N):
      for j in range(N):
        for k in range(4):
          ni = i + di[k]
          nj = j + dj[k]
          if 0<=ni<N and 0<=nj<N:         # 유효한 인덱스면
            print(arr[ni][nj])
    ```

<br/>

## ✨ 2차원 배열의 활용

- 전치 행렬

    ```python
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    for i in range(3):
      for j in range(3):
        if i < j:
          arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```

<br/>

## ✨ 부분집합

- 집합의 원소가 n개일 때, 부분집합의 개수는 2^n개 (공집합 포함)

- **비트 연산자**

    - `&` : 비트 단위로 and 연산
    - `|` : 비트 단위로 or 연산
    - `<<` : 피연산자의 비트 열을 왼쪽으로 이동
    - `>>` : 피연산자의 비트 열을 오른쪽으로 이동
    - `1<<n` : 2^n. 즉 **원소가 n개일 경우의 모든 부분집합의 수**를 의미

    - `i & (1<<j)` : i의 j번째 비트가 1인지 아닌지를 검사

- **비트 연산자를 활용한 부분집합 생성**

    ```python
    arr = [1, 2, 3]
    n = len(arr)
    
    for i in range(1<<n):                # 부분집합의 개수
      for j in range(n):                 # 원소의 수 만큼 비트를 비교
        if i & (1<<j):                   # i의 j번 비트가 1인 경우
          print(arr[j], end=', ')        # j번 원소 출력
      print()
    print()
    ```

<br/>

## ✨ 검색

- 탐색 키 : 자료를 구별하여 인식할 수 있는 키
- **검색의 종류**
    - 순차 검색
    - 이진 검색
    - 해쉬 