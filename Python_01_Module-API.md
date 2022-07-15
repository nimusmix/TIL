# Python_01_Module-API

## ✨Module

- 함수나 변수 등을 모아놓은 파이썬 파일
- `import` 로 모듈을 삽입한 후, 모듈 내의 함수나 변수를 불러올 때는 `모듈명.변수`를 써야 함.

``` python
# random이라는 모듈을 삽입함.
import random

# random 모듈의 sample 함수 불러오기
numbers = range(1, 46)
lucky = random.sample(numbers, 6)
```



## ✨API

- 먼저 `pip install 라이브러리명`를 터미널에 입력해서 설치해야 함.

``` python
# requests라는 라이브러리 삽입
# requests는 url에 가서 정보를 요청하고, 서버가 응답한 정보를 가져오는 라이브러리

import requests

# url 입력
# jun이라는 정보를 요청하는 url
url = 'https://api.agify.io/?name=jun'

# json 형식으로 가져온 파일 프린트
print(requests/get(url).json())
```



## ✨Lotto

```python
import random

winner = [10, 14, 16, 18, 29, 35]
numbers = range(1, 46)

# for문으로 풀기
for chance in range(7000000):
    lucky = random.sample(numbers, 6)
    member = 0
    for i in range (6):
        if lucky[i] in winner:
            member += 1
    if member == 6:
        
        print("same")
				print(chance)

# while문으로 풀기
chance = 0
while member != 6:
    lucky = random.sample(numbers, 6)
    chance += 1
    member = 0
    for i in range (6):
        if lucky[i] in winner:
            member += 1
    if member == 6:
        print("same")
```

