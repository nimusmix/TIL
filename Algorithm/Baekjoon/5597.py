list = []

for i in range(28):
    num = int(input())
    list.append(num)
    
for i in range(1, 31):
    if i not in list:
        print(i)