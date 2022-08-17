# Algorithm_08_0817

## ✨ 스택의 특성

- 선형구조 (자료 간의 관계가 1대1의 관계)
- 후입선출 (**LIFO**, Last-In-First-Out)
- 배열을 사용할 수 있음.
- 마지막에 삽입된 원소의 위치를 **top**이라 부름.

<br/>

## ✨ 스택의 연산

- 삽입 (`push`) : 저장소에 자료를 저장함.

    ```python
    def push(item, size):
      global top
      top += 1
      if top == size:
        print('overflow!')          # 디버깅용
      else:
        stack[top] = item
    
    size = 10
    stack = [0] * size
    top = -1
    
    print(push(10, size))
    
    # push(20)과 똑같은 기능을 하는 코드
    top += 1
    stack[top] = 20
    ```

- 삭제 (`pop`) : 저장소에서 자료를 꺼냄.

    ```python
    def pop():
      global top
      if top == -1:
        print('underflow!')         # 디버깅용
        return 0
      else:
        top -= 1
        return stack[top+1]
      
    print(pop())
    
    # pop()과 똑같은 기능을 하는 코드
    if top > -1:
      top -= 1
      print(stack[top+1])
    ```

- `isEmpty` : 스택이 공백인지 아닌지를 확인하는 연산

- `peek` : 스택의 top에 있는 item을 반환하는 연산

<br/>

## ✨ 스택 구현 고려사항

- 1차원 배열을 사용하여 구현할 경우 **구현이 용이하다는 장점**이 있지만, **스택의 크기를 변경하기 어렵다는 단점**이 존재

<br/>

## ✨ 스택의 응용 (괄호검사)

- 괄호의 종류 : `[]`, `{}`, `()`
- 조건
    1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
    2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
    3. 괄호 사이에는 포함 관계만 존재한다.

- 알고리즘 개요
    1. 여는 괄호를 만나면 `push(여는 괄호)`
    2. 닫는 괄호를 만나면 `pop()` 하여 괄호 간 짝 비교
    3. 괄호 수식이 끝났는데 스택에 괄호가 남아 있거나 닫는 괄호가 남아 있으면 오류

<br/>

## ✨ 스택의 응용 (Function Call)

- 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로,
    스택을 이용하여 수행순서 관리
- 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를
    stack frame에 저장하여 시스템 스택에 삽입
- 함수의 실행이 끝나면 시스템 스택의 top 원소(stack frame)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
- 함수의 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 됨.

<br/>

## ✨ 재귀 호출

```python
# 팩토리얼
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * f(n-1)

for i in range(21):
  print(factorial(i))
  
# 피보나치1
def fibo1(n):
  if n < 2:
    return n
  else:
    return fibo1(n-1) + fibo1(n-2)
  
for i in range(101):
  print(fibo1(i))
  
# 피보나치2
def fibo2(n):
  if memo[n] == -1:
    memo[n] = fibo2(n-1) + fibo(n-2)
  return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1

for i in range(101):              # Memoization. 속도가 fibo1보다 훨씬 빠름!
  print(fibo2(i))
```

<br/>

## ✨ Memoization

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술

```python
# memoization을 적용한 fibonacci
def fibo(n):
  if n >= 2 and len(memo) <= n:
    memo.append(fibo(n-1) + fibo(n-2))
   return memo[n]

memo = [0, 1]
```

<br/>

## ✨ DP (Dynamic Programming)

- = 동적 계획 알고리즘
- 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여,
    최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘
- 최적화 문제를 해결하는 알고리즘
- 구현 방식
    - recursive 방식
    - iterative 방식
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문에
        memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적

```python
# DP 적용 피보나치 알고리즘1
def fibo1(n):
  f = [0, 1]
  
  for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])  
  return f[n]

# DP 적용 피보나치 알고리즘2
def fibo2(n):
  f[0] = 0
  f[1] = 1
  
  for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]
  return

f = [0] * 101
fibo2(100)
print(f[100])
```

<br/>

## ✨ DFS (깊이 우선 탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 **모든 자료를 빠짐없이 검색**하는 것이 중요
    - 깊이 우선 탐색(**DFS**; Depth First Search) 또는 너비 우선 탐색(**BFS**; Breath First Search)을 통해 탐색

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면,
    가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여
    결국 모든 정점을 방문하는 순회방법

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

- 방법

    1. 시작 정점 v를 결정하여 방문한다.

    2. 정점 v에 인접한 정점 중에서

        1️⃣ 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고 정점 w를 방문한다.
              그리고 w를 v로 하여 다시 2를 반복한다.

        2️⃣ 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위하여
              스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다.

    3. 스택이 공백이 될 때까지 2를 반복한다.

```python
adjList = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]

visted = [0] * N                      # 1. 배열 visited를 False로 초기화
stack = [0] * N                       # 2. 공백 스택 생성
top = -1

def dfs(v, N):                        # 시작 정점, 정점 개수
  print(v)
  visited[v] = 1                      # 3. 시작점 방문 표시
  while True:
    for w in adjList[v]:              # 4. v의 인접 정점 중 방문 안 한 정점 w가 있으면
      if visited[w] == 0:
        top += 1                      # 5. push(v)
        stack[top] = v
        v = w
        print(v)
        visited[w] = 1
        break
    else:                             # 6. v의 인접 정점 중 방문 안한 정점 w가 없으면
      if top != -1:                   # 7. 스택이 비어 있지 않은 경우
        v = stack[top]                # 8. pop(v)
        top -= 1
      else:                           # 9. 스택이 비어 있으면 while문 break
        break
 
dfs(0, 7)
```

```python
'''
0번부터 V번까지, E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

V, E = map(int, input().split())
N = V+1
adjList = [[] for _ in range(N)]

for _ in range(E):                     # 위 주석 데이터로 adjList 만들기
  a, b = map(int, input().split())
  adjList[a].append(b)
  adjList[b].append(a)
  
visited = [0] * N

def dfs(v):
  print(v)
  visited[v] = 1
  for w in adjList[v]:
    if visited[w] == 0:
      dfs(w)
```