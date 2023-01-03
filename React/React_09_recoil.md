# React_09_recoil

## ✨ install

```bash
npm i recoil
```

```react
// index.tsx
...
import { RecoilRoot } from 'recoil';

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <div>
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </RecoilRoot>
  </div>,
);
```

<br/>

## ✨ using

- `useRecoilValue(atom)`

```typescript
// atoms.ts
import { atom } from "recoil";

export const isDarkAtom = atom({
  key: 'isDark',
  default: false
})
```

```react
// App.tsx
...
import { lightTheme, darkTheme } from './theme';
import { useRecoilValue } from 'recoil';
import { isDarkAtom } from './atoms';
...
function App() {
  const isDark = useRecoilValue(isDarkAtom);
  return (
    <>
      <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
        <Reset />
        <GlobalStyle />
        <Router />
        <ReactQueryDevtools initialIsOpen />
      </ThemeProvider>
    </>
  );
}
```

<br/>

## ✨ modifying

- `useSetRecoilState(atom)`

```react
// coins.tsx
...
import { useSetRecoilState } from 'recoil';
import { isDarkAtom } from '../atoms';

function Coins() {
  const setDarkAtom = useSetRecoilState(isDarkAtom);
  const toggleDarkAtom = () => setDarkAtom((prev) => !prev);

  return (
    <Container>
      <Header>
        <Title>Coins</Title>
        <button onClick={toggleDarkAtom}>mode</button>
      </Header>
      ...
    </Container>
  );
}
```

