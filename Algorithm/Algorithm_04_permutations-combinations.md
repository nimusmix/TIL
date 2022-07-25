# Algorithm_04_permutations-combinations

## ✨ 순열 (Permutations)

- `permutations(iterable, r)`
- iterable에 대해 중복을 허용하지 않고 r개를 뽑아서 나열
- 뽑힌 순서대로 나열하기 때문에 순서가 유의미함.

```python
import itertools

for i in permutations([1,2,3], 2):
  print(i, end=" ")
  
# (1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2)
```

<br/>

## ✨ 조합 (Combinations)

- `combinations(iterable, r)`
- iterable에 대해 중복을 허용하지 않고 r개를 뽑아서 나열
- 뽑은 순서는 고려하지 않음.

```python
import itertools

for i in combinations([1,2,3], 2):
  print(i, end=" ")
  
# (1, 2) (1, 3) (2, 3)
```