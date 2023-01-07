# React_07_react-query

## ✨ install

```bash
npm i react-query
npm i @tanstack/react-query
```

```react
// index.tsx
...
import { QueryClient, QueryClientProvider } from 'react-query';

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <div>
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <App />
      </ThemeProvider>
    </QueryClientProvider>
  </div>,
);
```

<br/>

## ✨ useQuery

- `useQuery<interface>('signiture', fetcher, {refetchInterval: })`

```typescript
// api.ts
import axios from 'axios';

const BASE_URL = 'https://api.coinpaprika.com/v1'

export async function axiosCoinInfo(coinId: string) {
  const res = await axios.get(`${BASE_URL}/coins/${coinId}`);
  return res.data
}

export async function axiosCoinPrice(coinId: string) {
  const res = await axios.get(`${BASE_URL}/tickers/${coinId}`);
  return res.data
}
```

```react
// Coin.tsx
...
import { useQuery } from 'react-query';
import { axiosCoinInfo, axiosCoinPrice } from '../api';

function Coin() {
  const { coinId } = useParams<RouteParams>();
  const { state } = useLocation<RouteState>();
  const { isLoading: infoLoading, data: info } = useQuery<Info>(['info', coinId], () => axiosCoinInfo(coinId));
  const { isLoading: priceLoading, data: price } = useQuery<Price>(['price', coinId], () => axiosCoinPrice(coinId), {
    refetchInterval: 10000,
  });
  const chartMatch = useRouteMatch('/:coinId/chart');
  const priceMatch = useRouteMatch('/:coinId/price');
  const loading = infoLoading || priceLoading;
  ...
```

<br/>

## ✨ dev tools

```react
// App.tsx
...
import { ReactQueryDevtools } from 'react-query/devtools';

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
```
