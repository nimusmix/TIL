# React_01

## ✨ Quick Start

```bash
npx create-react-app app-name
cd app-name
npm start
```

<br/>

## ✨ Prop Types

```bash
npm i prop-types
```

```javascript
// src/Button.js
import PropTypes from 'prop-types'

function Button({txt}) {
  return <button>{txt}</button>
}

Button.propTypes = {
  txt: PropTypes.string.isRequired
}

export default Button;
```

<br/>

## ✨ CSS Module

```css
/* src/Button.module.css */
.btn {
  background-color: gray;
  color: white;
  padding: 10px 15px;
  border: 0;
  border-radius: 10px;
}
```

```javascript
// src/Button.js
import styles from "./Button.module.css"

function Button({txt}) {
  return (
    <button className={styles.btn}>              // 랜덤으로 className 생성됨.
      {txt}
    </button>
  )
}
...
```

<br/>

## ✨ useEffect

```javascript
import { useEffect } from 'react';               // 자동으로 작성됨.

function App() {
  console.log('all time');
  
  useEffect(() => {
    console.log('once')
  }, []);                                        // 처음 render될 때만 실행됨.
  
  useEffect(() => {
    if (keyword) {
      console.log('when keyword changes')
    }
  }, [keyword]);                                 // keyword가 변경될 때만 실행됨.
}
```

- `useEffect(effect, deps)`

- 코드를 언제 실행할 것인지 선택할 수 있음.

- Cleanup

    ```javascript
    function cleanUp() {  
      useEffect(() => {
        console.log('created')
        return () => console.log('destroyed')    // destroy될 때 return문 실행됨.
      }, [])
    }
    ```

    
