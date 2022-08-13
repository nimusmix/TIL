A, B, V = map(int, input().split())

print((V-B)//(A-B) if (V-B) % (A-B) == 0 else (V-B)//(A-B)+1)