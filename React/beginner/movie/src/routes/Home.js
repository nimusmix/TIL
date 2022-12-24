import React, { useState, useEffect } from 'react';
import Movie from '../components/Movie';
import styles from './Home.module.css'

function Home() {
  const [loading, setLoading] = useState(true)
  const [movies, setMovies] = useState([])

  const getMovies = async() => {
    // 같은 코드
    // const json = await (await fetch('https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year')).json()
    const response = await fetch('https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year')
    const json = await response.json()

    setMovies(json.data.movies)
    setLoading(false)
  }

  useEffect(() => {
    getMovies()
  }, [])

  return (
    <div className={styles.container}>
      {loading ? <div className={styles.loader}>Loading ...</div> : (
        <div className={styles.movies}>
          {movies.map((movie) => (
            <Movie
              key={movie.id}
              id={movie.id}
              year={movie.year}
              coverImg={movie.medium_cover_image}
              title={movie.title}
              summary={movie.summary}
              genres={movie.genres}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Home;