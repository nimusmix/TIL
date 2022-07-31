x, y, w, h = list(map(int, input().split()))

row = min([abs(x-0), abs(x-w)])
column = min([abs(y-0), abs(y-h)])

print(min([row, column]))