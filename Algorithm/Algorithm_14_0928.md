# Algorithm_14_0928

## ✨ 상호 배타 집합 (Disjoint-sets)

- 서로소 또는 상호 배타 집합들은 서로 중복 포함된 원소가 없는 집합들을 말함. (교집합이 없음.)

- 집합에 속한 하나의 특정 멤버(대표자)를 통해 각 집합들을 구분

- 상호 배타 집합을 표현하는 방법

    - 연결 리스트
    - 트리

- 상호 배타 집합 연산

    - `Make-set(x)` : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

        ```python
        def make_set(x):
            p[x] = x
        ```

    - `Find-set(x)` : x를 포함하는 집합을 찾는 연산

        ```python
        def find_set(x):
            while p[v] != v:
                v = p[v]
            return v
        ```

    - `Union(x, y)` : x와 y를 포함하는 두 집합을 x를 대표자로 하여 통합하는 연산

        ```python
        def union(x, y):
            r1 = find_set(x)                     # x의 대표 원소를 찾고
            r2 = find_set(y)                     # y의 대표 원소를 찾아서
            p[r2] = r1                           # y의 대표 원소를 x의 대표 원소로 교체
        ```


- 연산의 효율을 높이는 방법
    - Rank를 이용한 Union
        - 각 노드는 자신을 루트로 하는 subtree의 높이를 `rank`라는 이름으로 저장
            - 두 집합을 합칠 때 `rank`가 낮은 집합을 `rank`가 높은 집합에 붙임.
    - Path compression
        - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 변경

<br/>

## ✨ 최소 비용 신장 트리 (MST)

- 그래프에서 최소 비용 문제
    1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
    2. 두 정점 사이의 최소 비용의 경로 찾기
- 신장 트리 : n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
- **최소 신장 트리 (Minimum Spanning Tree)** ⭐️
    : 무방향 가중치 그래프에서 **신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리**

- MST를 표현하는 방법
    - 그래프
    - 간선들의 배열
    - 인접 리스트
    - 부모 자식 관계와 가중치에 대한 배열
        - 트리

<br/>

## ✨ Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
    1. 임의 정점을 하나 선택해서 시작
    2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
    3. 모든 정점이 선택될 때까지 1, 2를 반복
- 서로소인 2개인 집합(2 disjoint-sets) 정보를 유지
    - 트리 정점들 (tree vertices) : MST를 만들기 위해 선택된 정점들
    - 비트리 정점들 (nontree vertices) - 선택되지 않은 정점들

```python
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim1(r, V):
    MST = [0]*(V+1)                             # MST 포함 여부
    key = [10000]*(V+1)                         # 가중치의 최대값 이상으로 초기화
                                                # key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0                                  # 시작정점의 key
    for _ in range(V):                          # V+1개의 정점 중 V개를 선택
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:   # MST에 포함되지 않은 정점 중 key가 최소인 u 찾기
                u = i
                minV = key[i]
        MST[u] = 1                              # 정점 u를 MST에 추가
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:  # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
                key[v] = min(key[v], adjM[u][v] # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)                             # MST 가중치의 합

def prim2(r, V):                                # prim1보다 간단
    MST = [0]*(V+1)                             # MST 포함 여부
    MST[r] = 1                                  # 시작 정점 표시
    s = 0                                       # MST 간선의 가중치 합
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            # MST에 포함된 정점 i와 인접한 정점 j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w                              # 가중치가 있는 무방향 그래프

print(prim1(0, V))
print(prim2(0, V))
```

<br/>

## ✨ Kruskal 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
    1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
    2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴.
        (사이클이 존재하면 다음으로 가중치가 낮은 간선 선택)
    3. n-1개의 간선이 선택될 때까지 2를 반복

```python
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())                # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, v, u])                      # sort 위해 w를 맨 앞으로 하여 append
edge.sort()
rep = [i for i in range(V+1)]                   # 대표원소 배열
N = V + 1                                       # 정점 수
cnt = 0                                         # 선택한 edge의 수
total = 0                                       # MST 가중치의 합
for w, v, u in edge:
    if find_set(v) != find_set(u):              # 사이클 거르기 (대표원소가 다를 때만 MST에 포함)
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:                          # MST 구성이 끝나면 (MST의 간선 수 = 정점 수 - 1)
            break
print(total)
```

<br/>

## ✨ 최단 경로

- 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
    - 다익스트라(dijkstra) 알고리즘 : 음의 가중치 허용 X
    - 벨만-포드(Bellman-Ford) 알고리즘 : 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
    - 플로이드-워샬(Floyd-Warshall ) 알고리즘

<br/>

## ✨ Dijkstra 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작 정점 s에서 끝 정점 t까지의 최단 경로에 정점 x가 존재함.
- 이 때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로로 구성됨.
- 탐욕 기법을 사용한 알고리즘으로, MST의 프림 알고리즘과 유사함.

```python
'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

def dijkstra(s, V):
    U = [0]*(V+1)                               # 비용이 결정된 정점을 표시
    U[s] = 1                                    # 출발점 비용 결정
    for i in range(V+1):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):                          # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점w 중에서
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(V+1):                    # 비용 결정
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w]+adjM[w][v])

INF = 10000
V, E = map(int, input().split())
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0]*(V+1)
dijkstra(0, V)
print(D)
```
