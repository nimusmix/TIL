import { useState, useEffect } from 'react';

function App() {
  const [loading, setLoading] = useState('true')
  const [coins, setCoins] = useState([])
  const [budget, setBudget] = useState('')
  const [canBuy, setCanBuy] = useState('')

  const budgetChange = (event) => setBudget(event.target.value)
  const coinChange = (event) => {
    const selectedCoin = coins.find((coin) => coin.name === event.target.value)
    setCanBuy(`${budget / selectedCoin.quotes.USD.price} ${selectedCoin.symbol}`)
  }

  useEffect(() => {
    fetch('https://api.coinpaprika.com/v1/tickers')
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      })
  }, [])

  return (
    <div>
      <h1>The Coins {loading ? null : `(${coins.length})`}</h1>
      {loading ? <strong>Loading ...</strong> :
        <div>
          <input
            onChange={budgetChange}
            value={budget}
            type='number'
            placeholder='Enter you budget.'
          >
          </input>
          <select onChange={coinChange}>
            <option>Select the coin you want.</option>
            {coins.map((coin) => <option key={coin.id}>{coin.name}</option>)}
          </select>
          <p>{canBuy ? `You can buy ${canBuy}.` : null}</p>
          
          <ul>
            {coins.map((coin) => 
              <li key={coin.id}>{coin.name} ({coin.symbol}) : {coin.quotes.USD.price} USD</li>
            )}
          </ul>
        </div>
      }
    </div>
  );
}

export default App;
