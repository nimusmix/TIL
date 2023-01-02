import { createGlobalStyle } from 'styled-components';
import { Reset } from 'styled-reset';
import Router from './Router';
import { ReactQueryDevtools } from 'react-query/devtools';

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
    color: inherit;
  }
`;

function App() {
  return (
    <>
      <Reset />
      <GlobalStyle />
      <Router />
      <ReactQueryDevtools initialIsOpen />
    </>
  );
}

export default App;
