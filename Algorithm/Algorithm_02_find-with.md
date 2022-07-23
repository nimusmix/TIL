# Algorithm_02_find-with

## ✨ find()

- 문자열에서 특정 문자열을 찾아 index를 리턴
- 찾는 문자열이 없을 경우 **-1**을 리턴

```python
# find(찾는 문자[, 시작 위치])
word = 'apple'
word.find('p')       # 1
word.find('p', 2)    # 2
word.find('p', 3)    # -1
```



## ✨startswith(), endwith()

- 문자열이 특정 문자열로 시작하는지 또는 끝나는지 여부를 리턴

```python
word = 'apple'

# startswith(시작하는 문자[, 시작 위치])
word.startswith('a')         # True
word.startswith('p')         # False
word.startswith('p', '1')    # True

# endswith(끝나는 문자[, 시작 위치[, 끝 위치])
word.endswith('e')           # True
word.endswith('l', 1, 4)     # Ture
```

