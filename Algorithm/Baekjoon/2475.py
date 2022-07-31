n = [i ** 2 for i in list(map(int, input().split()))]

print(sum(n) % 10)