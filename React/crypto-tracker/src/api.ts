import axios from 'axios';

const BASE_URL = 'https://api.coinpaprika.com/v1'

export async function axiosCoins() {
  const res = await axios.get(`${BASE_URL}/coins`);
  return res.data.slice(0, 100);
}

export async function axiosCoinInfo(coinId: string) {
  const res = await axios.get(`${BASE_URL}/coins/${coinId}`);
  return res.data
}

export async function axiosCoinPrice(coinId: string) {
  const res = await axios.get(`${BASE_URL}/tickers/${coinId}`);
  return res.data
}

export async function axiosCoinHistory(coinId: string) {
  const res = await axios.get(`https://ohlcv-api.nomadcoders.workers.dev?coinId=${coinId}`)
  return res.data
}