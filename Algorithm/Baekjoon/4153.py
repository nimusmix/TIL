while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a*a + b*b == c*c:
        print('right')
    else:
        print('wrong')