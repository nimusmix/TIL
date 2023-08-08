def count(n):
    cnt = 0
    bin_n = bin(n)[2:]
    bin_n_len = len(bin_n)
    
    for i in range(bin_n_len):
        if bin_n[i] == '1':
            val = bin_n_len - i - 1
            cnt += square_sum[val]
            cnt += n - 2 ** val + 1
            n = n - 2 ** val
            
    return cnt


A, B = map(int, input().split())
square_sum = [0] * 60

for i in range(1, 60):
    square_sum[i] = 2 ** (i-1) + 2 * square_sum[i-1]

print(count(B) - count(A-1))