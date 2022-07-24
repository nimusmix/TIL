# Algorithm_03_fibonacci

## ✨ Recursion function

```python
def fibo(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibo(n-2) + fibo(n-1)
```



## ✨ List update

```python
fibo = [0, 1]

for i in range(2, n+1):
  fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[n])
```



## ✨ Variable

```python
a = 0
b = 1

for i in range(n):
    a, b = b, a+b    # a, b를 같은 줄에 쓰지 않으면 윗줄부터 실행되어 a에 b가 먼저 할당되고 b = b+b가 됨.
                     # a, b = b, a+b는 한번에 실행되므로 a가 변겅되지 않음.

print(a)
```

