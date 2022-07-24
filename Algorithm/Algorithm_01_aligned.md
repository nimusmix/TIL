# Algorithm_01_aligned

## ✨ Right aligned

- `.rjust(n)` : 전체 n 중 오른쪽 정렬

```python
# 별 찍기 오른쪽 정렬
a = int(input())

for i in range(a):
    print(('*' * i).rjust(a))
```

<br/>

## ✨ Center

- `.center(n)` : 전체 n 중 가운데 정렬

```python
# 별 찍기 가운데 정렬
a = int(input())

for i in range(a):
    print(('*' * i).center(a))
```
