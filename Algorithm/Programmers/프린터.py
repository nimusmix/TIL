from collections import deque

def solution(priorities, location):
    ans = 0
    target = (location, priorities[location])
    queue = deque([(idx, i) for idx, i in enumerate(priorities)])
    
    while queue:
        max_v = max(queue, key=lambda x:x[1])
        
        idx, i = queue.popleft()
        if (idx, i) == max_v:
            ans += 1
            if (idx, i) == target:
                return ans
        else:
            queue.append((idx, i))