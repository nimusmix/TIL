# React_02_router

## ✨ install

```bash
npm i react-router-dom
```

- src 내에 routes 폴더, components 폴더 생성하기

<br/>

## ✨ react-router-dom

```javascript
// src/App.js
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './routes/Home';
import Detail from './routes/Detail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' exact element={<Home />}/>
        <Route path='/movie/:id' element={<Detail />}/>
      </Routes>
    </Router>
  ); 
}

export default App;
```

- `exact`
    - true일 경우, url이 정확히 일치할 때만 이동함.

<br/>

```javascript
// src/routes/Detail.js
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Detail() {
  const { id } = useParams();
  const [movie, setMovie] = useState('')

  useEffect(() => {
    const getMovie = async() => {
      const json = await (
        await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
      ).json()
      setMovie(json.data.movie)
    }

    getMovie();
  }, [id]);
  
  return (
    <div>
      <h1>Detail</h1>
      <h3>{movie.title}</h3>
    </div>
  );
}

export default Detail;
```

- `useParams()`
    - 동적 url의 파라미터를 얻을 수 있음.
