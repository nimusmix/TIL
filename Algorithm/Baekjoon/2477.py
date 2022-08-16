N = int(input())

di = [list(map(int, input().split())) for _ in range(6)]
nested = []
print(di)

for idx, i in enumerate(di):
    if i[0] == di[idx-2][0]:
        nested.append(i[0])

nested = nested*2
r_nested = nested.reverse()

print(nested)
print(di[0:4][0])