from collections import deque, defaultdict
from itertools import combinations

# n: 장소의 개수, edges: 장소 사이의 길, users: 장소마다의 유저 수
# d: 유저가 이동 가능한 거리, limit: 수용 가능한 최대 바이크 수
# 파킹존은 2개만 설치

def solution(n, edges, users, d, limit):
    adj = [[0] * (n+1) for _ in range(n+1)]
    available = defaultdict(list)                                # 노드를 key로 하고 해당 노드에 접근 가능한 사람들을 value로 하는 dict
    
    for edge in edges:                                           # 인접 행렬 생성
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]
        
    for idx, user in enumerate(users):
        available[idx+1].extend([idx+1] * user)                  # 각 노드에 주어진 인원을 available에 추가
        
        
    def bfs(node, moved, visited):
        nonlocal available
        queue = deque()
        queue.append((node, moved, visited))
        
        while queue:
            n, m, v = queue.pop()
            for idx, i in enumerate(adj[n]):                     # 해당 노드의 인접 행렬을 순회하며
                if i != 0 and (m + i) <= d and idx not in v:     # 길이 연결되어 있고, 이동 가능한 거리 안이고, 아직 방문하지 않았다면
                    queue.append((idx, m + i, v + [idx]))        # queue에 추가
                    available[idx].extend([n] * users[n-1])      # available에도 인원 추가
            
    for n in range(1, n+1):                                      # 각 노드마다 bfs 돌면서 available 만들기
        bfs(n, 0, [])
    
    ans = 0
    for combi in combinations(range(1, n+1), 2):                 # 주어진 노드에서 2개를 뽑는 모든 경우의 수 탐색
        i, j = combi
        list1 = available[i][:]
        list2 = available[j][:]
        
        if list1 == [] or list2 == []:                           # 하나라도 비어 있으면 다음 조합을 탐색함.
            continue
        
        idx = cnt = 0
        while idx < len(list1) and cnt < limit * 2:              # idx가 list1의 길이보다 작고, cnt가 최대보다 작은 동안
            if list1[idx] in list2:                              # list1과 list2에 모두 존재하는 user 먼저 제거
                cnt += 1
                idx2 = list2.index(list1[idx])
                list1.pop(idx)
                list2.pop(idx2)
            else:
                idx += 1
        
        if cnt < limit * 2:
            for _ in range(limit):
                if list1:
                    cnt += 1
                    list1.pop()
                    
                if cnt >= limit * 2:
                    break
        
        # 여기도 if cnt < limit * 2: 를 했어야 하는데...
            for _ in range(limit):
                if list2:
                    cnt += 1
                    list2.pop()
                    
                if cnt >= limit * 2:
                    break

        ans = max(cnt, ans)
    return ans



# 6
print(solution(7, [[1, 2, 2], [5, 2, 2], [1, 5, 2], [1, 3, 1], [1, 6, 2], [1, 7, 3], [6, 7, 4], [7, 4, 1]], [0, 2, 0, 0, 0, 4, 1], 2, 3))
# 4
print(solution(3, [[1, 2, 1], [3, 2, 1]], [1, 2, 1], 1, 2))
# 3
print(solution(3, [[1, 2, 2], [3, 2, 2]], [1, 2, 1], 1, 2))
# 6
print(solution(6, [[1, 2, 1], [2, 3, 1], [3, 6, 1], [6, 5, 1], [4, 5, 1], [4, 1, 1]], [1, 1, 1, 1, 1, 1], 1, 3))