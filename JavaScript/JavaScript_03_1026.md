# JavaScript_03_1026

## ✨ 동기와 비동기

- 동기
  - 모든 일을 순서대로 하나씩 처리하는 것
    (이전 작업이 끝나면 다음 작업을 시작함.)
- 비동기
  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적 수행)
  - 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
  - 비동기를 사용하는 이유는 사용자 경험 때문
    - 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에
      마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨.
    - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로,
      사용자 경험에 긍정적인 효과를 볼 수 있음.

<br/>

## ✨ JavaScript의 비동기 처리

- Single Thread 언어
  - JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로
    동시에 여러 작업을 처리할 수 없음.
- JavaScript Runtime
  - JavaScript는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
  - 특정 언어가 동작할 수 있는 환경을 런타임(Runtime)이라 함.
  - JavaScript에서 비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리

<br/>

## ✨ 브라우저 환경에서의 비동기 동작

- **구성 요소**
  1. JavaScript Engine의 `Call Stack`
     - 요청이 들어올 때마다 순차적으로 처리하는 Stack (LIFO)
     - 기본적인 JavaScript의 Single Thread 작업 처리
  2. `Web API`
     - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로 시간이 소요되는 작업을 처리
       (setTimeout, DOM Event, AJAX 요청 등)
  3. `Task Queue`
     - 비동기 처리된 Callback 함수가 대기하는 Queue (FIFO)
  4. `Event Loop`
     - Call Stack과 Task Queue 지속적으로 모니터링
     - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push
- **동작 방식**
  1. 모든 작업은 `Call Stack(LIFO)`으로 들어간 후 처리된다.
  2. 오래 걸리는 작업이 `Call stack`으로 들어오면 `Web API`로 보내서 처리하도록 한다.
  3. `Web API`에서 처리가 끝난 작업들은 `Task Queue(FIFO)`에 순서대로 들어간다.
  4. `Event Loop`가 `Call Stack` 이 비어 있는 것을 체크하고, `Task Queue`에서 가장 오래된 작업을 `Call Stack`으로 보낸다.
- 즉, JavaScript는 Single Thread 언어로 동기적 처리를 하지만,
  브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐
  Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨.

<br/>

## ✨ Axios 라이브러리

- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, 브라우저 환경은 CDN을 이용해서 사용할 수 있음.

<br/>

## ✨ Axios 기본 구조

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios.get('요청할 URL')
  .then(성공하면 수행할 콜백 함수)
  .catch(실패하면 수행할 콜백 함수)
</script>
```

<br/>

## ✨ 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리한다는 것
- 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음.
  ➡ 실행 결과를 예상하면서 코드를 작성할 수 없음.
  ➡ 콜백 함수 사용으로 해결

<br/>

## ✨ 콜백 함수

- 다른 함수의 인자로 전달되는 함수

- 동기, 비동기 상관 없이 사용 가능

- 시간이 걸리는 비동기 작업이 완료된 후 실행될 작업을 명시하는 데 쓰이는 콜백 함수를 **비동기 콜백**이라 함.

- 예시

  ```javascript
  // JavaScript
  btn.addEventListener('click', () => alret('Completed'))
  ```

  ```python
  # Django
  urlpatterns = [
      path('index/', views.index),
  ]
  ```

- 사용하는 이유
  - 명시적인 호출이 아닌 특정한 조건 혹은 행동에 호출되도록 작성할 수 있음.
  - "요청이 들어오면", "이벤트가 발생하면", "데이터를 받아오면" 등의 조건으로 이후 로직을 제어할 수 있음.
  - 즉, 비동기 처리를 순차적으로 동작할 수 있게 함.
  - 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요

<br/>

## ✨ 프로미스 (Promise)

- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체

- "작업이 끝나면 실행시켜줄게"라는 약속

- 비동기 작업의 완료 또는 실패를 나타내는 객체

- Promise 기반의 클라이언트가 바로 Axios 라이브러리

- `then()`

  - 요청한 작업이 성공하면 callback 실행
  - callback은 이전 작업의 **성공 결과**를 인자로 전달 받음.

- `catch()`

  - `then()`이 하나라도 실패하면 callback 실행
  - callback은 이전 작업의 **실패 객체**를 인자로 전달 받음.

- then과 catch 모두 항상 promise 객체를 반환 ➡ then을 계속 이어 나가며 작성할 수 있음.

  ```javascript
  axios.get('요청할 URL')
    .then(성공하면 수행할 1번 콜백 함수)
    .then(1번 콜백 함수가 성공하면 수행할 2번 콜백 함수)
    .then(2번 콜백 함수가 성공하면 수행할 3번 콜백 함수)
    .catch(어디서든 실패하면 수행할 콜백 함수)

- 비교

  ```javascript
  // 기존의 콜백 함수 작성 방식
  work1(function () {
    // work1
    work2(result1, function (result2) {
      // work2
      work3(result2, function (result3) {
        console.log('최종 결과 : ' + result3)
      })
    })
  })
  
  // promise 방식
  work1()
    .then((result1) => {
      // work2
      return result2
    })
    .then((result2) => {
      // work3
      return result3
    })
    .catch((error) => {
      // error handling
    })
  ```

- promise 방식은 비동기 처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음.

<br/>

## ✨ Promise가 보장하는 것 (vs 비동기 콜백)

1. 콜백 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음.
   Promise 방식은 Event Queue에 배치되는 엄격한 순서로 호출됨.
2. 비동기 작업이 성공하거나 실패한 뒤에 `then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. `then()`을 여러 번 사용하여 여러 개의 콜백 함수를 추가할 수 있음. (Chaining)
   - 각각의 콜백은 주어진 순서대로 하나하나 실행하게 됨.

<br/>

## ✨ Axios의 다른 표기법

```javascript
// 1
axios.get('요청할 URL')

// 2
axios({
  method: 'get',
  url: '요청할 URL',
})

// ex
axios({
  method: 'post',
  url: '요청할 URL',
  data: {
    title: '제목',
    content: '내용'
  }
})
```

- 1번과 2번은 동일하게 동작하나 2번이 데이터를 추가하기 용이함.
- Axios 홈페이지의 요청 Config 카테고리 참고하여 속성값 작성하실 것.

<br/>

## ✨ AJAX

- 비동기 통신을 이용하면 화면 전체를 새로고침하지 않아도 서버로 요청을 보내고 데이터를 받아
  화면의 일부분만 업데이트 가능
- 이러한 '비동기 통신 웹 개발 기술'을 **AJAX**(Asynchronous Javascript And XML)이라 함.
- AJAX의 특징
  1. 페이지 새로고침 없이 서버에 요청
  2. 서버로부터 응답을 받아 작업을 수행
- 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

<br/>

## ✨ 비동기 적용 - Follow

- 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성

  ```html
  <!-- base.html -->
  <body>
    ...
    {% block script %}
    {% endblock script%}
  </body>
  ```

- axios CDN 작성

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
    </script>
  {% endblock script %}
  ```

- form 요소 선택을 위해 id 속성 지정 및 선택
  불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문)

  ```html
  <!-- accounts/profile.html -->
  <form id="follow-form">
    ...
  </form>
  ...
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
    </script>
  {% endblock script %}
  ```

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()                                      <!-- 여기! -->
      })
    </script>
  {% endblock script %}
  ```

- axios 요청 준비

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        axios({                                                     <!-- 여기! -->
          method: 'post',
          url: `/accounts/${???}/follow/`,
        })
      })
    </script>
  {% endblock script %}
  ```

- url에 작성할 user_pk 가져오기 (HTML -> JavaScript)

  - data-* attributes

    - 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법

    - 예를 들어 `data-test-value`라는 이름의 특성을 지정했다면
      JavaScript에서는 `element.dataset.testValue`로 접근할 수 있음.

    - 속성명 작성 시 주의사항

      1. 대소문자 여부에 상관 없이 xml로 시작하면 안됨.
      2. 세미콜론을 포함해서는 안됨.
      3. 대문자를 포함해서는 안됨.

    - 예시

      ```html
      <div data-my-id="my-data"></div>
      <script>
        const myId = event.target.dataset.myId
      </script>
      ```

  ```html
  <!-- accounts/profile.html -->
  <form id="follow-form" data-user-id="{{ person.pk }}">
    ...
  </form>
  ...
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId                  <!-- 여기! -->
        axios({
          method: 'post',
          url: `/accounts/${userId}/follow/`,
        })
      })
    </script>
  {% endblock script %}
  ```

- hidden 타입으로 숨겨져 있는 csrf 값을 가진 input 태그를 선택

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  {% endblock script %}
  ```

- AJAX로 csrf token을 전송

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        axios({
          method: 'post',
          url: `/accounts/${userId}/follow/`,
          headers: {'X-CSRFToken': csrftoken,}
        })
      })
    </script>
  {% endblock script %}
  ```

- 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답

  ```python
  # accounts/views.py
  from django.http import JsonResponse
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          User = get_user_model()
          me = request.user
          you = User.objects.get(pk=user_pk)
          if me != you:
              if you.followers.filter(pk=me.pk).exists():
                  you.followers.remove(me)
                  is_followed = False
              else:
                  you.followers.add(me)
                  is_followed = True
              context = {
                  'is_followed': is_followed,
              }
              return JsonResponse(context)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')
  ```

- view 함수에서 응답한 is_followed를 사용해 버튼 토글

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      const form = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        axios({
          method: 'post',
          url: `/accounts/${userId}/follow/`,
          headers: {'X-CSRFToken': csrftoken,}
        })
          .then((response) => {
            const isFollowed = response.data.is_followed
            const followBtn = document.querySelector('#follow-form > input[type=submit]')
            if (isFollowed === true) {
              followBtn.value = '언팔로우'
            } else {
              followBtn.value = '팔로우'
            }
          })
      })
    </script>
  {% endblock script %}
  ```

<br/>

## ✨ XHR

- XML Http Request
- AJAX 요청을 생성하는 JavaScript API
- XHR의 메서드로 브라우저와 서버 간 네트워크 요청을 전송할 수 있음.
- Axios는 손쉽게 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리

<br/>

## ✨ 비동기 적용 - 팔로잉 & 팔로워 수 비동기 적용

- 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성

  ```html
  <!-- accounts/profile.html -->
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> / 
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
  </div>
  ```

- 직전에 작성한 span 태그를 각각 선택

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      ...
        axios({
          method: 'post',
          url: `/accounts/${userId}/follow/`,
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            ...
            const followersCountTag = document.querySelector('#followers-count')
            const followingsCountTag = document.querySelector('#followings-count')
          })
      })
    </script>
  {% endblock script %}
  ```

- 팔로잉, 팔로워 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

  ```python
  # accounts/views.py
  from django.http import JsonResponse
  
  @require_POST
  def follow(request, user_pk):
      ...
              context = {
                  'is_followed': is_followed,
                  'followers_count': you.followers.count(),
                  'followings_count': you.followings.count(),
              }
              return JsonResponse(context)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')
  ```

- view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경

  ```html
  <!-- accounts/profile.html -->
  {% block script %}
    <script>
      ...
        axios({
          method: 'post',
          url: `/accounts/${userId}/follow/`,
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            ...
            const followersCountTag = document.querySelector('#followers-count')
            const followingsCountTag = document.querySelector('#followings-count')
            const followersCount = response.data.followers_count
            const followingsCount = response.data.followings_count
            followersCountTag.innerText = followersCount
            followingsCountTag.innerText = followingsCount
          })
      })
    </script>
  {% endblock script %}
  ```

<br/>

## ✨ 비동기 적용 - 좋아요

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>좋아요 : <span id="likes-{{ article.pk }}">{{ article.like_users.all|length }}</span>개</p>
    <div>
      <form class="like-forms" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
        {% else %}
          <input type="submit" value="좋아요" id="like-{{ article.pk }}">
        {% endif %}
      </form>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}

{% block script %}
  <script>
    const forms = document.querySelectorAll('.like-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    forms.forEach((form) => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.articleId
        
        axios({
          method: 'post',
          url: `/articles/${articleId}/likes/`,
          headers: {'X-CSRFToken': csrftoken,}
        })
          .then((response) => {
            const isLiked = response.data.is_liked
            const likeBtn = document.querySelector(`#like-${articleId}`)
            if (isLiked === true) {
              likeBtn.value = '좋아요 취소'
            } else {
              likeBtn.value = '좋아요'
            }
            const likesCountTag = document.querySelector(`#likes-${articleId}`)
            const likesCount = response.data.likes_count
            likesCountTag.innerText = likesCount
          })
      })
    })
  </script>
{% endblock script %}
```

```python
from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likes_count': article.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```
