def is_prime(x):
    if x == 1:
        return False    
    root = int(x ** 0.5)
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    if is_prime(num):
        cnt += 1
        
print(cnt)