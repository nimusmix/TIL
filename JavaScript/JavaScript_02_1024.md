# JavaScript_02_1024

## ✨ Browser APIs

- 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함.

- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음.
- 종류
  - DOM
  - Geolocation API : 지리 정보
  - WebGL 등 : 그래픽

<br/>

## ✨ DOM

- 문서 객체 모델 (Document Object Model)
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움.
  - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음.
- HTML 문서를 구조화하여 각 요소를 객체로 취급
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능함.
- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음.
- 웹 페이지는 일종의 문서이고, 그 문서는 웹 브라우저를 통해 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함.
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음.

<br>

## ✨ DOM의 주요 객체

- window
- document
- navigator, location, history, screen 등

<br/>

## ✨ DOM의 주요 객체 - window

- DOM을 표현하는 창

- 가장 최상위 객체 (작성 시 생략 가능)

- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄.

- window의 메서드 예시

  ```javascript
  // 새 탭 열기
  window.open()
  
  // 경고 대화 상자 표시
  window.alert()
  
  // 인쇄 대화 상자 표시
  window.print()
  ```

<br/>

## ✨ DOM의 주요 객체 - document

- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함하고 있음.
- document 또한 windows의 속성

<br/>

## ✨ DOM 조작 - 선택

- 선택 관련 메서드

  - `document.querySelector(selector)`

    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)

    ```javascript
    console.log(document.querySelector('#title'))
    // <h1 id='title'>JS기초</h1>
    ```

  - `document.querySelectorAll(selector)`

    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자로 받음.
    - 제공한 CSS selector를 만족하는 NodeList를 반환

    ```javascript
    console.log(document.querySelectorAll('.text'))
    // NodeList(2) [p.text, p.text]
    
    console.log(document.querySelecotrAll('body > ul > li'))
    // NodeList(2) [li, li]
    ```

<br/>

## ✨ DOM 조작 - NodeList

- index로만 각 항목에 접근 가능
- 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
- `querySelectorAll()`에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음.

<br/>

## ✨ DOM 조작 - 조작

- 조작 관련 메서드 (생성)

  - `document.createElement(tagName)`

    - 작성한 tagName의 HTML 요소를 생성하여 반환

    ```javascript
    const h1Tag = document.createElement('h1')
    // <h1></h1>
    ```

- 조작 관련 메서드 (입력)

  - `Node.innerText`

    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
    - 사람이 읽을 수 있는 요소만 남김.
    - 즉, 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨.

    ```javascript
    h1Tag.innerText = 'DOM 조작'
    // <h1>DOM 조작</h1>
    ```

- 조작 관련 메서드 (추가)

  - `Node.appendChild()`

    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 한 번에 오직 하나의 Node만 추가할 수 있음.
    - 추가된 Node 객체를 반환
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

    ```javascript
    divTag = document.querySelector('div')
    divTag.appendChild(h1Tag)
    ```

- 조작 관련 메서드 (삭제)

  - `Node.removeChild()`

    - DOM에서 자식 Node를 제거
    - 제거된 Node를 반환

    ```javascript
    divTag.removeChild(h1Tag)
    ```

- 조작 관련 메서드 (속성 조회 및 설정)

  - `Element.getAttribute(attributeName)`
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
  - `Element.setAttribute(name, value)`
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 속성을 추가

  ```javascript
  const aTag = document.createElement('a')
  aTag.setAttribute('href', 'https://google.com')
  aTag.innerText = '구글'
  
  const divTag = document.querySelector('div')
  divTag.appendChild(aTag)
  ```

  ```javascript
  const h1Tag = document.querySelector('h1')
  h1Tag.classlist.toggle('blue')
  ```

<br/>

## ✨ Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고,
  특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음.
- DOM 요소는 Event를 **수신**하고, 받은 Event를 **처리**할 수 있음.
- Event 처리는 주로 `addEventListener()`라는 Event 처리기(Event Handler)를 다양한 html 요소에 **부착**해서 처리함.

<br/>

## ✨ Event Handler

- addEventListener

  - `EventTarget.addEventListener(type, listener[, options])`

  - 지정한 Event가 대상에 전달될 대마다 호출할 함수를 설정
  - Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
  - type
    - 반응할 Event 유형을 나타내는 대소문자 구분 문자열
    - 대표 이벤트 : `input`, `click`, `submit`
  - listener
    - 지정된 타입의 Event를 수신할 객체
    - JavaScript function 객체(콜백 함수)여야 함.
    - 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음.

  ```javascript
  // 버튼을 클릭하면 특정 변수 값 변경하기
  const btn = document.querySelector('#btn')
  btn.addEventListener('click', function (event) {
    const pTag = document.querySelector('#counter')
    countNum += 1
    pTag.innerText = countNum
  })
  ```

  ```javascript
  // input에 입력하면 입력 값을 실시간으로 출력하기
  const textInput = document.querySelector('#text-input')
  textInput.addEventListener('input', function (event) {
    const pTag = document.querySelector('p')
    pTag.innerText = event.target.value
  })
  ```

  ```javascript
  // input에 입력하면 입력 값을 실시간으로 출력하고, 버튼을 클릭하면 출력된 값의 클래스를 토글하기
  const textInput = document.querySelector('input')
  textInput.addEventListener('input', function (event) {
    const h1Tag = document.querySelector('h1')
    h1Tag.innerText = event.target.value
  })
  
  const btn = document.querySelector('#btn')
  btn.addEventListener('click', function (event) {
    const h1Tag = document.querySelector('h1')
    h1Tag.classList.toggle('blue')
  })
  ```

<br/>

## ✨ Event 취소

- `event.preventDefault()`

  - 현재 Event의 기본 동작을 중단
  - HTML 요소의 기본 동작을 작동하지 않게 막음.
  - HTML 요소의 기본 동작 예시
    - a 태그 : 클릭 시 특정 주소로 이동
    - form 태그 : form 데이터 전송

  ```javascript
  // 복사 금지하기
  const h1Tag = document.querySelector('h1')
  h1Tag.addEventListener('copy', function (event) {
    event.preventDefault()
    alert('복사할 수 없습니다.')
  })
  ```

<br/>

## ✨ Event 종합 실습

- 버튼을 클릭하면 랜덤 로또 번호 6개 출력하기

```javascript
const btn = document.querySelector('#lotto-btn')
btn.addEventListener('click', function (event) {
    
  // 공이 들어갈 컨테이너 생성
  const ballContainer = document.createElement('div')
  ballContainer.classlist.add('ball-container')
    
  // 랜덤한 숫자 6개 생성 (lodash 사용)
  const numbers = _.sampleSize(_.range(1, 46), 6)
  
  // 공 만들기
  numbers.forEach((number) => {
    const ball = document.createElement('div')
    ball.innerText = number
    ball.classlist.add('ball')
    ball.style.backgroundColor = 'Crimson'
    ballContainer.appendChild(ball)
  })
    
  // 공 컨테이너를 결과 영역의 자식으로 넣기
  const resultDiv = document.querySelector('#result')
  resultDiv.appendChild(ballContainer)
})
```

<br/>

## ✨ Event 종합 실습 2

- CREATE, READ 기능을 충족하는 todo app 만들기

```javascript
const formTag = document.querySelector('form')

const addTodo = function (event) {
  event.preventDefault()
  const inputTag = document.querySelector('.inputData')
  const data = inputTag.value
  
  if (data.trim()) {                                // 양 옆 공백을 제거하고 값이 있을 때
    const liTag = document.createElement('li')
    liTag.innerText = data
      
    const ulTag = document.querySelector('ul')
    ulTag.appendChild(liTag)
      
    event.target.reset()
  } else {                                         // 값이 없을 때
    alert('내용을 입력하세요.')
  }
}

formTag.addEventListner('submit', addTodo)
```

<br/>

## ✨ this

- 어떠한 object를 가리키는 키워드 (Python의 self와 유사)
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음.
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐.
- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고,
  함수를 호출할 때 **함수가 어떻게 호출되었는지에 따라 동적으로 결정**

<br/>

## ✨ 전역 문맥에서의 this

```javascript
console.log(this)                                  // window
```

- 브라우저의 전역 객체인 window를 가리킴.
- 전역 객체는 모든 객체의 유일한 최상위 객체를 의미

<br/>

## ✨ 함수 문맥에서의 this

1. 단순 호출

   ```javascript
   const myFunc = function () {
     console.log(this)                            // window (브라우저), global(Node.js)
   }
   ```

   - 전역 객체를 가리킴.
   - 브라우저에서는 window, Node.js는 global을 의미

2. Method (Function in Object)

   ```javascript
   const myObj = {
     data: 1,
     myFunc() {
       console.log(this)                         // myObj
       console.log(this.data)                    // 1
     }
   }
   
   myObj.myFunc()                                // myObj
   ```

   - 메서드로 선언하고 호출한다면 객체의 메서드이므로 해당 객체가 바인딩

3. Nested

   ```javascript
   // Function 키워드
   const myObj = {
     numbers = [1],
     myFunc() {
       console.log(this)                        // myObj
       this.numbers.forEach(function (number) {
         console.log(number)                    // 1
         console.log(this)                      // window
       })
     }
   }
   
   // 화살표 함수
   const myObj = {
     numbers = [1],
     myFunc() {
       console.log(this)                        // myObj
       this.numbers.forEach((number) => {
         console.log(number)                    // 1
         console.log(this)                      // myObj
       })
     }
   }
   ```

   - forEach 콜백 함수에서의 this는 단순 호출 방식으로 사용되었기 때문에
     메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴.
   - 이를 해결하기 위해 등장한 함수 표현식이 화살표 함수
   - 화살표 함수에서 this는 자신을 감싼 정적 범위
   - 자동으로 한 단계 상위의 scope의 context를 바인딩
   - 화살표 함수
     - 호출의 위치와 상관 없이 상위 스코프를 가리킴. (Lexical scope)
     - Lexical Scope : 함수를 어디서 호출하는지가 아니라 **어디에 선언하였는지**에 따라 결정
                                  Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식

<br/>

## ✨ this와 addEventListener

- addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함.
- 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩됨.
- 그러므로 **addEventListener의 콜백 함수는 function 키워드를 사용하기**

<br/>

