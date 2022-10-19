# JavaScript_01_1019

## ✨ 연산자

- **논리 연산자**

    - `&&` : and
    - `||` : or
    - `!` : not

- **삼항 연산자**

    - 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
    - 가장 앞의 조건식이 참이면 `:` 앞의 값이 반환되며, 반대의 경우 `:` 뒤의 값이 반환
    - 변수에 할당 가능

    ```javascript
    true ? 1 : 2
    false ? 1 : 2
    const result = Math.PI > 4 ? 'Yep' : 'Nope'
    ```

<br/>

## ✨ 조건문

- **if statement**

    - 조건 표현식의 결과를 boolean 타입으로 변환 후 참/거짓을 판단

    ```javascript
    if (name === 'admin') {
      console.log('관리자님 환영합니다.')
    } else if (name === 'manager') {
      console.log('매니저님 환영합니다.')
    } else {
      console.log(`${name}님 환영합니다.`)
    }
    ```

- **switch statement**

    - 조건 표현식의 결과값이 어느 case에 해당하는지 판별
    - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음.

    ```javascript
    switch(name) {
      case 'admin': {
        console.log('관리자님 환영합니다.')
        break
      }
      case 'manager': {
        console.log('매니저님 환영합니다.')
        break
      }
      default: {
        console.log(`${name}님 환영합니다.`)
      }
    }
    ```

<br/>

## ✨ 반복문

- **while**

    ```javascript
    let i = 0
    while (i < 6) {
      console.log(i)
      i += 1
    }
    ```

- **for**

- - const 사용 불가 (최초 정의한 변수를 재할당하며 사용하기 때문)

    ```java
    for ([초기문]; [조건문]; [증감문]) {
      // do something
    }
    
    for (let i = 0; i < 6; i++) {
      console.log(i)
    }
    ```

- **for ... in**

    - **객체**의 속성을 순회할 때 사용
    - 속성 이름을 통해 반복

    ```javascript
    const fruits = { a: 'apple', b: 'banana' }
    
    for (const key in fruits) {
      console.log(key)                                 // a, b
      console.log(fruits[key])                         // apple, banana
    }
    ```

- **for ... of**

    - 반복 가능한 객체를 순회할 때 사용 (Array, Set, String 등)
    - 속성 값을 통해 반복

    ```javascript
    const numbers = [0, 1, 2, 3]
    
    for (const number of numbers) {
      console.log(number)                              // 0, 1, 2, 3
    }
    ```

    

<br/>

## ✨ 함수

- **함수 정의 방법**

    - 함수 선언식

        - 호이스팅이 발생하여 사용을 권장하지 않음.

        ```javascript
        function add(num1, num2) {
          return num1 + num2
        }
        
        console.log(add(2, 5))
        ```

    - **함수 표현식**

        ```javascript
        const add = function (num1, num2) {
          return num1 + num2
        }
        
        console.log(add(2, 5))
        ```

        - 표현식에서 함수 이름을 명시하는 것도 가능하지만, 호출에 사용되지는 못하고 디버깅 용도로만 사용됨.

            ```javascript
            const add = function namedAdd(num1, num2) {
              return num1 + num2
            }
            
            console.log(add(2, 5))                      // 7
            console.log(namedAdd(2, 5))                 // ReferenceError
            ```

- **기본 인자**

    - 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

        ```javascript
        const greeting = function (name = 'Sumin') {
          return `Hi, ${name}!`
        }
        
        greeting()                                      // Hi, Sumin!
        ```

- **매개변수와 인자의 개수 불일치 허용**

    ```javascript
    const noArgs = function () {
      return 0
    }
    
    noArgs(1, 2, 3)                                     // 0
    ```

    ```javascript
    const twoArgs = function (arg1, arg2) {
      return [arg1, arg2]
    }
    
    twoArgs(1, 2, 3)                                    // [1, 2]
    ```

    ```javascript
    const threeArgs = function (arg1, arg2, arg3) {
      return [arg1, arg2, arg3]
    }
    
    threeArgs(1)                                        // [1, undefined, undefined]
    ```

- **Spread syntax (전개 구문)**

    - 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를
        배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음.

    - 배열

        ```javascript
        let parts = ['shoulders', 'knees']
        let lyrics = ['head', ...parts, 'and', 'toes']
        ```

    - 함수 (rest parameters)

        - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음.

        ```javascript
        const restParameters = function (arg1, arg2, ...restArgs) {
          return [arg1, arg2, restArgs]
        }
        
        console.log(restParameters(1, 2, 3, 4, 5))      // [1, 2, [3, 4, 5]]
        console.log(restParameters(1, 2))               // [1, 2, []]
        ```

<br/>

## ✨ 화살표 함수 (Arrow Function)

```javascript
const arrow = function (name) {
  return `Hello, ${name}!`
}

// 1. function 키워드 생략
const arrow1 = (name) => {
  return `Hello, ${name}!`
}

// 2. 매개변수가 하나일 경우, () 생략
const arrow2 = name => {
  return `Hello, ${name}!`
}

// 3. 함수의 내용이 return을 포함한 표현식 1개일 경우, {}와 return 생략
const arrow3 = name => `Hello, ${name}!`
```

- 단계

    1. function 키워드 생략
    2. 함수의 매개변수가 하나일 경우, `()` 생략
    3. 함수의 내용이 한 줄이라면 `{}`와 `return` 생략

- 화살표 함수는 항상 익명 함수이므로, 함수 표현식에서만 사용 가능

- 명확성과 일관성을 위해 항상 인자 주위에는 `()`을 포함하는 것을 권장

- Arrow Function 응용

    ```javascript
    // 1. 인자가 없다면 () or _로 표시 가능
    const noArgs = () => 'No args'
    const noArgs2 = _ => 'No args'
    
    // 1-1. object를 return한다면 return을 명시적으로 적어줘야 함.
    const returnObject = () => { return { key: 'value' } }
    
    // 1-2. return을 적지 않으려면 괄호를 붙여야 함.
    const returnObject2 = () => ({ key: 'value' })
    ```

<br/>

## ✨ 즉시 실행 함수 (IIFE)

```javascript
(function(num) { return num ** 3 })(2)                 // 8
(num => num ** 3)(2)                                   // 8
```

- 함수의 선언 끝에 `()`을 추가하여 선언되자마자 실행하는 형태
- 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음.
- 이러한 특징을 살려 초기화 부분에 많이 사용
- 일회성 함수이므로 익명함수로 사용하는 것이 일반적

<br/>

## ✨ Array와 Object

- JavaScript의 데이터 타입 중 참조 타입에 해당하는 타입은 **array**(배열) 와 **object**(객체)
- array는 인덱스를 key로 가지며 length 속성을 갖는 특수한 객체
- 객체 안쪽의 속성들은 메모리에 할당되어 있고 해당 객체는 메모리의 시작 주소 값을 기리키고 있는 형태로 이루어져 있음.

<br/>

## ✨ 배열 (Array)

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징이 있음.
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 `array.length` 형태로 접근 가능
    (배열의 마지막 원소는 `array.legnth - 1`로 접근)

<br/>

## ✨ Array Methods

|     메서드      |                             설명                             |
| :-------------: | :----------------------------------------------------------: |
|     reverse     |            원본 배열 요소들의 순서를 반대로 정렬             |
|   push & pop    |          배열의 **가장 뒤에** 요소를 추가 또는 제거          |
| unshift & shift |          배열의 **가장 앞에** 요소를 추가 또는 제거          |
|    includes     |       배열에 특정 값이 존재하는지 판별 후 참/거짓 반환       |
|     indexOf     | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환<br/>요소가 없을 경우 -1 반환 |
|      join       | 배열의 모든 요소를 구분자를 이용하여 연결<br/>구분자 생략 시 쉼표를 기본 값으로 사용 |

<br/>

## ✨ Array Helper Methods

|   메서드    |                             설명                             |
| :---------: | :----------------------------------------------------------: |
| **forEach** |        배열의 각 요소에 대해 콜백 함수를 한 번씩 실행        |
|   **map**   |      콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환      |
| **filter**  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |
| **reduce**  |    콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환     |
|  **find**   |        콜백 함수의 반환 값이 참이면 해당 요소를 반환         |
|  **some**   |    배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환    |
|  **every**  |      배열의 모든 요소가 판별 함수를 통과하면 참을 반환       |

- **forEach**

    ```javascript
    array.forEach((element, index, array) => {
      // do something
    })
    ```

    ```javascript
    const colors = ['red', 'blue', 'green']
    
    // 1. 일단 사용해보기
    printClr = function (color) {
      console.log(color)
    }
    
    colors.forEach(printClr)
    
    // 2. 함수 정의를 인자로 넣기
    colors.forEach(function (color) {
      console.log(color)
    })
    
    // 3. 화살표 함수 적용하기
    colors.forEach((color) => console.log(color))
    ```

    - `array.forEach(callback(element[, index[, array]]))`
    - 콜백 함수를 배열의 각 요소에 대해 한 번씩 실행
    - 3가지 매개변수로 구성
        1. element : 배열의 요소
        2. index : 배열 요소의 인덱스
        3. array : 배열 자체
    - 반환 값 없음.
    - **break, continue 사용 불가능**

- **map**

    ```javascript
    array.map((element, index, array)) => {
      // do something
    }
    ```

    ```javascript
    const numbers = [1, 2, 3]
    
    // 1. 일단 사용해보기
    const doubleFunc = function (number) {
      return number * 2
    }
    
    const doubleNum = numbers.map(doubleFunc)
    console.log(doubleNum)
    
    // 2. 함수 정의를 인자로 넣기
    const doubleNum = numbers.map(function (number) {
      return number * 2
    })
    
    // 3. 화살표 함수 적용하기
    const doubleNum = numbers.map((number) => number * 2)
    ```

    - `array.map(callback(element[, index[, array]]))`
    - **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환**
    - 기존 배열 전체를 다른 형태로 바꿀 때 유용 **(forEach + return)**

- **filter**

    ```javascript
    array.filter((element, index, array) => {
      // do something
    })
    ```

    ```javascript
    const products = [
      { name: 'cucumber', type: 'vegetable'},
      { name: 'banana', type: 'fruit'},
      { name: 'carrot', type: 'vegetable'},
      { name: 'apple', type: 'fruit'},
    ]
    
    // 1. 일단 사용해보기
    const fruitFilter = function (product) {
      return product.type === 'fruit'
    }
    
    const fruits = products.filter(fruitFilter)
    console.log(fruits)
    
    // 2. 함수 정의를 인자로 넣기
    const fruits = products.filter(fucntion (product) {
      return product.type === 'fruit'
    })
    
    // 3. 화살표 함수 적용하기
    const fruits = products.filter((product) => product.type === 'fruit')
    ```

    - `array.filter(callback(element[, index[, array]]))`
    - **콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환**
    - 기존 배열의 요소들을 필터링할 때 유용

- **reduce**

    ```javascript
    array.reduce((acc, element, index, array) => {
      // do something
    }, initialValue)
    ```

    ```javascript
    const tests = [90, 90, 80, 77]
    
    // 1. 함수 정의를 인자로 넣기
    const sum = tests.reduce(function (total, x) {
      return total + x
    }, 0)
    
    // 2. 화살표 함수 적용하기
    const sum = test.reduce((total, x) => total + x, 0)
    
    // 평균 구하기
    const avg = test.reduce((total, x) => total + x, 0) / tests.length
    ```

    - `array.reduce(callback(acc, element[, index[, array]])[, initialValue])`
    - 콜백 함수를 배열의 각 요소에 대해 한 번씩 실행해서 하나의 결과값을 반환
    - **배열을 하나의 값으로 계산하는 동작이 필요할 때 사용**
    - map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음.
    - 주요 매개변수
        1. acc : 이전 콜백 함수의 반환 값이 누적되는 변수
        2. initialValue : 최초 콜백 함수 호출 시 acc에 할당되는 값, defalut 값은 배열의 첫 번째 값
                                   빈 배열의 경우 initialValue가 없으면 에러 발생

- **find**

    ```javascript
    array.find((element, index, array)) {
      // do something
    }
    ```

    ```javascript
    const avengers = [
      { name: 'Tony Stark', age: 45 },
      { name: 'Steve Rogers', age: 32 },
      { name: 'Thor', age: 40 },
    ]
    
    // 1. 함수 정의를 인자로 넣기
    const avenger = avengers.find(function (avenger) {
      return avenger.name === 'Tony Stark'
    })
    
    // 2. 화살표 함수 적용하기
    const avenger = avengers.find((avenger) => avenger.name === 'Tony Strak')
    ```

    - `array.find(callback(element[, index[, array]]))`
    - **콜백 함수의 반환 값이 참이면 조건을 만족하는 첫 번째 요소를 반환**
    - 찾는 값이 없으면 undefined 반환

- **some**

    ```javascript
    array.some((element, index, array) => {
      // do something
    })
    ```

    ```javascript
    const arr = [1, 2, 3, 4, 5]
    
    const result = arr.some((x) => x % 2 === 0)
    ```

    - `array.some(callback(element[, index[, array]]))`
    - **배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 true 반환**
    - 빈 배열은 항상 false 반환

- **every**

    ```javascript
    array.every((element, index, array) => {
      // do something
    })
    ```

    ```javascript
    const arr = [1, 2, 3, 4, 5]
    
    const result = arr.every((x) => x % 2 === 0)
    ```

    - `array.every(callback(element[, index[, array]]))`
    - **배열의 모든 요소가 주어진 판별 함수를 통과하면 true 반환**
    - 빈 배열은 항상 true 반환

<br/>

## ✨ 배열 순회 비교

```javascript
const chars = ['A', 'B', 'C', 'D']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}

// for ... of
for (const char of chars) {
  console.log(char)
}

// forEach
chars.forEach((char, idx) => {
  console.log(idx, char)
})

chars.forEach(char => console.log(char))
```

<br/>

## ✨ 객체 (Object)

```javascript
const myInfo = {
  name: 'jack',
  phoneNumber: '123456',
  'samsung product': {
    buds: 'Buds pro',
    galaxy: 'S99',
  },
}

console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].galaxy)
```

- 객체는 속성의 집합이며, 중괄호 내부에 Key-Value 쌍으로 표현
- key는 문자열 타입만 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입 가능 (함수 포함)
- 객체 요소 접근은 `.` 또는 `[]`로 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 대괄호 접근만 가능

<br/>

## ✨ 객체 관련 문법

1. **속성명 축약**

    - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 생략 가능

    ```javascript
    const books = ['Learning JavaScript', 'Learning Python']
    const magazines = ['Vogue', 'Elle']
    const bookShop = {
      books,
      magazines,
    }
    ```

2. **메서드명 축약**

    - 메서드 선언 시 function 키워드 생략 가능

    ```javascript
    const obj = {
      greeting() {
        console.log('Hi!')
      }
    }
    
    obj.greeting()
    ```

3. **계산된 속성명 사용** (computed property name)

    - 객체를 정의할 때 key 이름을 표현식을 이용하여 동적으로 생성 가능

    ```javascript
    const key = 'country'
    const value = ['한국', '미국']
    const myObj = {
      [key]: value,
    }
    
    console.log(myObj)                                  // { country: ['한국', '미국' ] }
    ```

4. **구조 분해 할당** ⭐️

    - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당

    ```javascript
    const userInfo = {
      name: 'Sumin Kim',
      userId: 'nimusmix',
      phone: '010-0000-0000',
      email: 'nimusmix@gmail.com',
    }
    
    const { name } = userInfo
    const { userId } = userInfo
    const { phone, email } = userInfo
    ```

5. **객체 전개 구문** (Spread Operator)

    - 객체 내부에서 객체 전개 가능
    - 얕은 복사에 활용 가능

    ```javascript
    const obj = { b: 2, c: 3, d: 4 }
    const newObj = { a: 1, ...obj, e: 5 }
    
    console.log(newObj)                                 // {a: 1, b: 2, c: 4, d: 4, e: 5}
    ```

6. **JSON**

    - JavaScript Object Notation
    - Key-Value 형태로 이루어진 자료 표기법
    - JavaScript의 object와 유사한 구조를 가지고 있지만,
        object는 그 자체로 타입이고, JSON은 형식이 있는 "문자열"
    - 즉, JSON을 object로 사용하기 위해서는 변환 작업이 필요

    ```javascript
    const jsonData = {
      coffee: 'Americano',
      icecream: 'Chocolate',
    }
    
    // object -> JSON
    const objToJson = JSON.stringify(jsonData)
    
    // JSON -> object
    const jsonToObj = JSON.parse(objToJson)
    ```