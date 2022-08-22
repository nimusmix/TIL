# Algorithm_09_0822

## ✨ 중위표기법과 후위표기법

- **중위표기법** (infix notation) : 연산자를 피연산자의 가운데 표기하는 방법  *ex) A+B*
- **후위표기법** (postfix notation) : 연산자를 피연산자 뒤에 표기하는 방법  *ex) AB+*

<br/>

## ✨ 문자열 수식 계산의 일반적 방법

1. 중위 표기법의 수식을 후위 표기법으로 변경한다. (스택 이용)

    1️⃣ 입력 받은 중위 표기식에서 토큰을 읽는다.

    2️⃣ 토큰이 피연산자이면 토큰을 출력한다.

    3️⃣ 토큰이 연산자(괄호 포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.

    4️⃣ 토큰이 오른쪽 괄호(`)`)이면 스택 top에 왼쪽 괄호(`(`)가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.

    5️⃣ 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.

    6️⃣ 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
          (스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.)

    ```python
    # icp (in-coming priority)
    # isp (in-stack priority)
    
    if icp > isp:
      push()
    else:
      pop()
    ```

    | 토큰 | isp  | icp  |
    | :--: | :--: | :--: |
    |  )   |  -   |  -   |
    | *, / |  2   |  2   |
    | +, - |  1   |  1   |
    |  (   |  0   |  3   |

2. 후위 표기법의 수식을 스택을 이용하여 계산한다.

    1️⃣ 피연산자를 만나면 스택에 push한다.

    2️⃣ 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push한다.
          (연산시 먼저 pop된 피연산자가 뒤로 가야 함!)

    3️⃣ 수식이 끝나면 마지막으로 스택을 pop하여 출력한다.

<br/>

## ✨ 백트래킹

- 해를 찾는 도중에 '막히면' 되돌아가서 다시 해를 찾아가는 기법
- 최적화 문제와 결정 문제를 해결할 수 있음.
    - 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'로 답하는 문제
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감.
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며,
    반대로 해답의 가능성이 있으면 유망하다고 함.
- 가지치기 (pruning) : 유망하지 않은 노드가 포함되는 경로는 더이상 고려하지 않는다.
- **백트래킹 알고리즘의 절차**
    1. 상대 공간 트리의 깊이 우선 검색을 실시한다.
    2. 각 노드가 유망한지를 점검한다.
    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속 한다.

```python
# chess. 퀸은 상하좌우대각선으로는 다른 체스말을 둘 수 없음.
def checkmode(v):                   # v == 퀸을 두는 위치
  if promising(v):
    if there is a solution at v:
      write the solution
    else:
      for u in each childe of v:
        checkmode(u)
```

<br/>

## ✨ 백트래킹 vs DFS

- 백트래킹은 가지치기를 통해 시도의 횟수를 줄임.
- DFS가 모든 경로를 추적하는 데에 비해 백트래킹은 불필요한 경로를 조기에 차단
- DFS를 가하기에는 경우의 수가 너무나 많음.
- 일반적으로 백트래킹 알고리즘을 적용하면 경우의 수가 줄어들지만 최악의 경우에는 여전히 지수함수시간을 요함.

<br/>

## ✨ 부분집합 구하기

- `powerset` : 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합

```python
# powerset을 구하는 백트래킹 알고리즘
def backtrack(a, k, input):
  global MAXCANDIDATES
  c = [0] * MAXCANDIDATES
  
  if k = input:
    process_solutuin(a, k)         # 답이면 원하는 작업을 한다.
  else:
    k += 1
    ncandidates = construct_candidates(a, k, input, c)
    
    for i in range(ncandidates):
      a[k] = c[i]
      backtrack(a, k, input)

def construct_candidates(a, k, input, c):
  c[0] = True
  c[1] = False
  return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)
```

```python
# 부분집합 구하기
def f(i, N):
  if i == N:
    for i in range(N):
      if bit[i]:
        print(A[i], end=' ')
    print()
  else:
    bit[i] = 1
    f(i+1, N)
    bit[i] = 0
    f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
f(0, 10)
```

```python
# 부분집합 합이 10이 되는 개수 구하기
def f(i, N):
  global ans
  if i == N:
    s = 0                           # 부분집합의 합을 담을 변수
    for i in range(N):
      if bit[i]:
        s += A[i]
    if s == 10:
      ans += 1                      # 부분집합의 합이 10인 경우의 수
  else:
    bit[i] = 1
    f(i+1, N)
    bit[i] = 0
    f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
f(0, 10)
```

```python
def f(i, N, s, t):                 # s == 이전 원소까지의 부분집합의 합, t == target
  global ans
  if i == N:                       # 모든 원소가 고려된 경우
    if s == t:                     # 부분집합의 합이 t이면
      ans += 1
    return
  elif s > t:
    return
  else:
    f(i+1, N, s+a[i], t)           # 부분집합에 A[i]가 포함된 경우
    f(i+1, N, s, t)                # 부분집합에 A[i]가 포함되지 않은 경우
  
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
f(0, 10, 0, 10)
```

<br/>

## ✨ 순열

```python
def f(i, N):
  if i == N:                       # 순열 완성
    print(P)
  for j in range(1, N):            # P[i]에 들어갈 숫자 P[j] 결정
    P[i], P[j] = P[j], P[i]
    f(i+1, N)
    P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, 3)
```