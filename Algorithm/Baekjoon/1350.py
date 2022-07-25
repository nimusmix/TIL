n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
c = 0

for i in files:
    if i % cluster == 0:
        c += i // cluster 
    else:
        c += i // cluster + 1
        
print(cluster * c)