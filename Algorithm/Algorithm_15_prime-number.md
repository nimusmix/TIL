# Algorithm_15_prime-number

## ✨ 소수 판별하기

```python
def is_prime(x):
    if i == 1:
      return False
    root = int(x ** 0.5)
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True
```

<br/>

## ✨ 에라토스테네스의 체

```python
def prime_list(x):
    sieve = [1] * x
    root = int(x ** 0.5)

    for i in range(2, root+1):
        if sieve[i] == True:
            for j in range(i+i, x, i):
                sieve[j] = False

    return [i for i in range(2, x) if sieve[i] == True]
```