# React_04_styled-components

## ✨ install

```bash
npm i styled-components
```

```javascript
import styled from 'styled-components' 
```

<br/>

## ✨ Basic

```react
const Wrapper = styled.div`
  display: flex;
`
const Box = styled.div`
  background-color: tomato;
  width: 100px;
  height: 100px;
`
const Text = styled.span`
  color: white;
`

function App() {
  return (
    <Wrapper>
      <Box>
        <Text>Hello!</Text>
      </Box>
      <Box />
    </Wrapper>
  )
}
```

<br/>

## ✨ Adapting

```react
const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`

function App() {
  return (
    <div>
      <Box bgColor='teal'/>
      <Box bgColor='tomato'/>
    </div>
  )
}
```

<br/>

## ✨ Extending

```react
const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`
const Circle = styled(Box)`
  border-radius: 50px;
`

function App() {
  return (
    <div>
      <Box bgColor='teal'/>
      <Circle bgColor='tomato'/>
    </div>
  )
}
```

<br/>

## ✨ As

```react
const Btn = styled.button`
  color: white;
  background-color: gray;
`

function App() {
  return (
    <div>
      <Btn as='a' href='/'>Log in</Btn>
    </div>
  )
}
```

<br/>

## ✨ Attrs

```react
const Input = styled.input.attrs({ required: true, minLength: 10 })`
  background-color: black;
`

function App() {
  return (
    <div>
      <Input/>
      <Input/>
    </div>
  )
}
```

<br/>

## ✨ Animations

```react
import styled, { keyframes } from 'styled-components'

const rotation = keyframes`
from {
  transform: rotate(0deg);
}
to {
  transform: rotate(360deg);
}
`
const Box = styled.div`
  background-color: gray;
  width: 100px;
  height: 100px;
  animation: ${rotation} 1s linear infinite
`

function App() {
  return (
    <div>
      <Box/>
    </div>
  )
}
```

```react
import styled, { keyframes } from 'styled-components'

const rotation = keyframes`
  0% {
    transform: rotate(0deg);
    border-radius: 0px;
  }
  50% {
    border-radius: 100px;
  }
  100% {
    transform: rotate(360deg);
    border-radius: 0px;
  }
`
const Box = styled.div`
  background-color: gray;
  width: 100px;
  height: 100px;
  animation: ${rotation} 1s linear infinite
`

function App() {
  return (
    <div>
      <Box/>
    </div>
  )
}
```

<br/>

## ✨ Pseudo Selectors

```react
const Emoji = styled.span`
  font-size: 36px;
`
const Box = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: gray;
  width: 200px;
  height: 200px;
  ${Emoji} {
    &:hover {
      font-size: 60px;
    }
    &:active {
      opacity: 0;
    }
  }
`

function App() {
  return (
    <div>
      <Box>
        <Emoji>💃</Emoji>
      </Box>
    </div>
  )
}
```

<br/>

## ✨ Theme

```javascript
// index.js
...
import { ThemeProvider } from 'styled-components'
import App from './App'

const darkTheme = {
  textColor: "whitesmoke",
  backgroundColor: "#111",
}

const lightTheme = {
  textColor: "#111",
  backgroundColor: "whitesmoke"
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ThemeProvider theme={darkTheme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>
)
```

```react
// App.js
const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background-color: ${(props) => props.theme.backgroundColor}
`
const Title = styled.h1`
  color: ${(props) => props.theme.textColor}
`

function App() {
  return (
    <Wrapper>
      <Title>Hello</Title>
    </Wrapper>
  )
}
```

