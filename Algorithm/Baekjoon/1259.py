import copy

while 1:
    n = list(input())
    m = copy.deepcopy(n)
    m.reverse()

    if n == ["0"]:
        break

    print('yes' if n == m else 'no')