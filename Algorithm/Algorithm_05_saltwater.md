# Algorithm_05_saltwater

## ✨ 소금물의 농도와 양 계산

n개의 소금물이 섞였을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램을 만드시오.

- **조건**
  
  1. 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.
  
  2. 최대 5개의 소금물을 입력할 수 있다.
  
  3. 출력된 혼합물의 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

- **입력 예시**
  
  ```python
  1. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오. : 1% 400g
  2. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오. : 8% 300g
  Done
  ```

- **출력 예시**
  
  ```python
  4.0% 700.0g
  ```

- **정답**
  
  ```python
  salt_list = []
  
  for i in range(1, 6):
      a = input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오. : ')
      if a == 'Done':
          break
      else:
          b = int(a[:a.find('%')])                 # % 전까지 슬라이싱
          c = int(a[a.find(' ')+1:a.find('g')])    # 공백+1부터 g 전까지 슬라이
          salt_list.append([b, c])
  
  salt = 0
  salt_water = 0
  
  for i in salt_list:
      salt += int(i[0])*int(i[1])
      salt_water += int(i[1])
  
  density = salt / salt_water
  
  print(f'{round(density,2)}% {round(salt_water,2)}g')
  ```
