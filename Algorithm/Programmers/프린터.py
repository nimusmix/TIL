def solution(priorities, location):
    answer = []
    
    max_v = max(priorities)
    while priorities:
        
        i = priorities.pop(0)
        if i == max_v:
            answer.append()
        else:
            priorities.append(i)
        
    
    return answer
            
# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))