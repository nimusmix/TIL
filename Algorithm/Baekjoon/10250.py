T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    room = N//H + 1
    
    if N % H == 0:
        floor = H
        room = N//H
        
    print(floor*100+room)