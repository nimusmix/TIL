t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    t_list = [[0] * 15 for _ in range(15)]
    p = 1

    for floor in range(15):
        for room in range(1, 15):
            if floor == 0:
                t_list[floor][room] = p
                p += 1
            else:
                t_list[floor][room] = t_list[floor-1][room] + t_list[floor][room-1]
    
    print(t_list[k][n])