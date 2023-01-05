import ApexCharts from 'react-apexcharts';
import { useQuery } from 'react-query';
import { useRecoilValue } from 'recoil';
import { axiosCoinHistory } from '../api';
import { isDarkAtom } from '../atoms';

function Price({ coinId }: IChart) {
  const isDark = useRecoilValue(isDarkAtom);
  const { isLoading, data } = useQuery<IData[]>(['ohlcv', coinId], () => axiosCoinHistory(coinId));
  return <h1>Price</h1>;
}

interface IChart {
  coinId: string;
}
interface IData {
  time_open: number;
  time_close: number;
  open: string;
  high: string;
  low: string;
  close: string;
  volume: string;
  market_cap: number;
}

export default Price;
