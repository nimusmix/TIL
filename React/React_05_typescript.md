# React_05_typescript

## ✨ install

```bash
npm create vite@latest name -- --template react-ts
```

<br/>

## ✨ style components

```bash
npm i styled-components
npm i -D @types/styled-components
```

<br/>

## ✨ interface

```react
import styled from 'styled-components';

function Circle({ bgColor }: CircleProps) {
  return <Container bgColor={bgColor} />;
}

interface CircleProps {
  bgColor: string;
}

interface ContainerProps {
  bgColor: string;
}

const Container = styled.div<ContainerProps>`
  width: 200px;
  height: 200px;
  background-color: ${(props) => props.bgColor};
  border-radius: 100px;
`;
```

<br/>

## ✨ optional props

```react
import styled from 'styled-components';

function Circle({ bgColor, borderColor }: CircleProps) {
  return <Container bgColor={bgColor} borderColor={borderColor ?? bgColor} />;
}

interface CircleProps {
  bgColor: string;
  borderColor?: string;
}

interface ContainerProps {
  bgColor: string;
  borderColor: string;
}

const Container = styled.div<ContainerProps>`
  width: 200px;
  height: 200px;
  background-color: ${(props) => props.bgColor};
  border-radius: 100px;
  border: 1px solid ${(props) => props.borderColor};
`;
```

<br/>

## ✨ forms

```react
import React, { useState } from 'react';

function App() {
  const [value, setValue] = useState('');
  const onChange = (event: React.FormEvent<HTMLInputElement>) => {
    const {
      currentTarget: { value },
    } = event;
    setValue(value);
  };
  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('hello', value);
  };

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input value={value} onChange={onChange} type="text" placeholder="username" />
        <button>Log in</button>
      </form>
    </div>
  );
}

export default App;
```

<br/>

## ✨ themes

- src 폴더 내에 `styled.d.ts`, `theme.ts` 생성

```react
// styled.d.ts
// theme의 interface 작성
import 'styled-components';

declare module 'styled-components' {
  export interface DefaultTheme {
    textColor: string;
    bgColor: string;
  }
}
```

```react
// theme.ts
import { DefaultTheme } from "styled-components";

export const lightTheme:DefaultTheme = {
  textColor: "black",
  bgColor: "white",
}

export const darkTheme:DefaultTheme = {
  textColor: "white",
  bgColor: "black",
}
```

```react
import styled from 'styled-components';

function App() {
  return (
    <div>
      <Container>
        <H1>Protected</H1>
      </Container>
    </div>
  );
}

const Container = styled.div`
  background-color: ${(props) => props.theme.bgColor};
`;
const H1 = styled.h1`
  color: ${(props) => props.theme.textColor};
`;

export default App;
```
