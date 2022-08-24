N = int(input())

for _ in range(N):
    vps = input()
    stack = []
    
    try:
        for i in vps:
                if i == '(': stack.append(i)
                else: stack.pop()
            
        if len(stack) == 0: print('YES')
        else: print('NO')
    except:
        print('NO')