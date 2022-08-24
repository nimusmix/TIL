# Algorithm_10_0824

## ✨ Queue의 기본 연산

- `enQueue(item)` : 삽입                             *rear 증가*
- `deQueue()` : 삭제                                     *front 증가*
- `createQueue()` : 공백 상태의 큐를 생성하는 연산
- `isEmpty()` : 큐가 공백 상태인지를 확인하는 연산
- `isFull()` : 큐가 포화 상태인지를 확인하는 연산
- `Qpeek()` : 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산

<br/>

## ✨ Queue의 상태 표현

```python
# 초기 상태
front == rear == -1

# 공백 상태
front == rear

# 포화 상태
rear == n-1                            # n == 배열의 크기, n-1 == 배열의 마지막 인덱스 
```

<br/>

## ✨ Queue의 구현

```python
# 삽입
def enQueue(item):
  global rear
  if isFull():
    print('Queue_Full')                  # 디버깅용
  else:
    rear += 1
    Q[rear] = item
    
# 삭제
def deQuque():
  global front
  if isEmpty():
    print('Queue_Empty')                 # 디버깅용
  else:
    front += 1
    return Q[front]
  
# 공백 상태 검사
def isEmpty():
  return front == rear

# 포화 상태 검사
def isFull():
  return rear == len(Q)-1

# 검색
def Qpeek():
  if isEmpty():
    print('Queue_Empty')                 # 디버깅용
  else:
    return Q[front+1]                    # 큐의 첫 번째에 있는 원소를 반환
```

<br/>

## ✨ 선형 큐 이용 시 문제점

- **잘못된 포화상태 인식**
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속 할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고
        `rear == n-1`인 상태 즉, 포화 상태로 인식하여 더이상의 삽입을 수행하지 않게 됨.
    - 해결방법
        1. 매 연산이 이루어질 때마다 원소들을 배열의 앞 부분으로 모두 이동시킴.
            원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐.
        2. 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용

<br/>

## ✨ 원형 큐의 구조

- 초기 상태 : `front == rear == 0`
- `front`와 `rear`의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 배열의 처음 인덱스인 0으로 이동해야 함.(나머지 연산자인 `mod`를 사용)
- 공백 상태와 포화 상태 구분을 쉽게 하기 위해 `front`가 있는 자리는 사용하지 않고 항상 빈자리로 둠.

|        |        삽입 위치        |         삭제 위치         |
| :----: | :---------------------: | :-----------------------: |
| 선형큐 |     rear = rear + 1     |     front = front + 1     |
| 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |

<br/>

## ✨ 원형 큐의 구현

```python
# 삽입
def enQueue(item):
  global rear
  if isFull():
    print('Queue_Full')                  # 디버깅용
  else:
    rear = (rear+1) % leb(cQ)
    cQ[rear] = item

# 삭제
def deQueue():
  global front
  if isEmpty():
    print('Queue_Empty')                 # 디버깅용
  else:
    front = (front + 1) % len(cQ)
    return cQ[front]

# 포화 상태 검사
def isFull():
  return (rear+1) % len(cQ) == front
```

<br/>

## ✨ 우선순위 큐

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨.
- 적용 분야
    - 시뮬레이션 시스템
    - 네트워크 트래픽 제어
    - 운영체제의 태스크 스케줄링

<br/>

## ✨ 우선순위 큐의 구현

- 배열을 이용한 우선순위 큐
- 리스트를 이용한 우선순위 큐

<br/>

## ✨ 배열을 이용한 우선순위 큐

- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선수위의 원소가 위치하게 됨.
- 문제점
    - 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
    - 이에 소요되는 시간이나 메모리 낭비가 큼.

<br/>

## ✨ 큐의 활용 (Buffer)

- 버퍼 : 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 데이터의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
- 버퍼의 자료 구조
    - 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨.
    - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨.

<br/>

## ✨ 마이쮸

```python
from collections import deque

p = 1                                  # 처음 줄 설 사람의 번호
q = deque()
N = 20                                 # 초기 마이쮸 개수
m = 0                                  # 나눠준 개수

while m < N:
  q.append((p, 1, 0))                  # 처음 줄 서는 사람
  v, c, my = q.popleft()
  # print(f'큐에 있는 사람 수: {len(q)+1}, 받아갈 사탕 수: {c}, 나눠준 사탕 수: {m}')
  m += c
  q.append((v, c+1, my+c))
  p += 1
print(f'마지막으로 받은 사람: {v}')
```

<br/>

## ✨ BFS (너비 우선 탐색)

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에,
    방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후 차례로 다시 BFS를 진행해야 하므로, **선입선출 구조의 큐를 사용**
- 출발점이 2개 이상이어도 탐색 가능
- 입력 파라미터 : 그래프 G와 탐색 시작점 v
- 방법
    1. 초기상태
        - visited 배열 초기화
        - queue 생성
        - 시작점 enqueue
    2. 시작점(A)부터 탐색 반복
        - dequeue A
        - A 방문한 것으로 표시
        - A의 인접점 enqueue
    3. queue가 비었을 때 탐색 종료

```python
def BFS(G, v):                           # 그래프 G, 탐색 시작점 v
  visited = [0] * (n+1)                  # n = 정점의 개수
  queue = []                             # 큐 생성
  queue.append(v)                        # 시작점 v를 큐에 삽입
  
  while queue:                           # 큐가 비어 있지 않은 경우
    t = queue.pop(0)                     # 큐의 첫 번째 원소 반환
    if not visited[t]:                   # 방문되지 않은 곳이라면
      visited[t] == True                 # 방문한 것으로 표시
      visit(t)                           # 정점 t에서 할 일
      for i in G[t]:                     # t와 연결된 모든 정점에 대해
        if not visited[i]:               # 방문되지 않은 곳이라면
          queue.append(i)                # 큐에 넣기
```

```python
def BFS(G, v, n):                        # 그래프 G, 탐색 시작점 v, 정점의 개수 n
  visited = [0] * (n+1)
  queue = []
  queue.append(v)
  visited[v] = 1
  
  while queue:
    t = queue.pop(0)
    visit(t)
    for i in G[t]:
      if not visited[i]:
        queue.append(i)
        visited[i] = visited[t] + 1      # t로부터 1만큼 더해 최단 경로 찾기 용이하게 함.
```

```python
# 출발점이 2개 이상인 BFS 탐색 (바이러스 확산)
def bfs(N):
    visited = [[0] * N for _ in range(N)]
    queue = []
    sec = 0                              # 바이러스 확산까지 몇 초 걸리는지 
    for i in range(N):
      for j in range(N):
        if virus[i][j] == 2:
          queue.append((i, j))
          visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)
        if virus[i][j] == 3:
            for k in visited:
                if max(k)-1 > sec:
                    sec = max(k)-1
            return sec
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and virus[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    virus = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {bfs(N)}')
```

<br/>

## ✨ DFS vs BFS

- A에서 B로 가는 경로가 있는가? ➡️  `DFS`, `BFS`

- A에서 B로 가는 경로의 개수는? ➡️ `DFS`

- A에서 B로 가는 최단 경로의 길이는? ➡️ 주로 `BFS` (`DFS`도 가능은 함.)

    - 최단경로 `DFS`

        - 모든 경로를 돌아봐야 한다는 단점이 존재

        ```python
        # ex) SWEA 4875 미로
        def dfs(i, j, s, N):
          global possible_route_cnt
          global shortest_distance
          if maze[i][j] == 3:
            possible_route_cnt += 1       # 가능한 경로의 수 cnt
            if shortest_distance > s+1:   # 출발, 도착 포함하므로 s에 +1
              shortest_distance = s+1
            return
          else:
            visited[i][j] = 1
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
              ni, nj = i+di, j+dj
              if 0<=ni<N and 0<=nj<n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, s+1, N)
            visited[i][j] = 0             # return 하기 전에 방문기록 지우기
            return
            
        N = int(input())
        maze = [list(map(int, input())) for _ in range(N)]
        
        sti = -1
        for i in range(N):
          for j in range(N):
            if maze[i][j] == 2:
              sti, stj = i, j
              break
          if sti != -1:
            break
        
        possible_route_cnt = 0
        shortest_distance = N*N
        visited = [[0]*N for _ in range(N)]
        
        dfs(sti, stj, 0, N)
        
        if shortest_distance = N*N:       # 최단경로가 초기에 설정한 그대로라면
          shortest_distance = -1          # 갈 수 있는 경로가 없다는 것이므로 -1
        
        print(possible_route_cnt)
        print(shortest_distance)
        ```
