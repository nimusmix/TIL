N = int(input())

words = []

for _ in range(N):
    N = input()
    NN = str(len(N))+N
    
    if NN not in words:
        words.append(NN)
    
words.sort()

for i in words:
    print(i[1:])