# React_06_styles

## ✨ CSS Reset

```bash
npm i styled-reset
```

```json
// App.tsx
import { Reset } from 'styled-reset'

function App() {
  return (
    <>
      <Reset />
    </>
  );
}
```

<br/>

## ✨ Global Style

```react
import { Reset } from 'styled-reset'
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Source Sans Pro', sans-serif;
    background-color: ${(props) => props.theme.bgColor};
    color: ${(props) => props.theme.textColor};
  }
  a {
    text-decoration: none;
  }
`;

function App() {
  return (
    <>
      <Reset />
      <GlobalStyle />
    </>
  );
}
```

