import ApexCharts from 'react-apexcharts';
import { useQuery } from 'react-query';
import { useRecoilValue } from 'recoil';
import { axiosCoinHistory } from '../api';
import { isDarkAtom } from '../atoms';

function Chart({ coinId }: IChart) {
  const isDark = useRecoilValue(isDarkAtom);
  const { isLoading, data } = useQuery<IData[]>(['ohlcv', coinId], () => axiosCoinHistory(coinId));
  return (
    <>
      {isLoading ? (
        'Loading Chart...'
      ) : (
        <ApexCharts
          type="line"
          series={[
            {
              name: 'price',
              data: data?.map((price) => parseFloat(price.close)) as number[],
            },
          ]}
          options={{
            theme: {
              mode: isDark ? 'dark' : 'light',
            },
            chart: {
              width: 440,
              height: 250,
              background: 'transparent',
              toolbar: {
                show: false,
              },
            },
            grid: {
              show: false,
            },
            stroke: {
              curve: 'smooth',
              width: 3,
            },
            xaxis: {
              axisTicks: { show: false },
              labels: { show: false },
              type: 'datetime',
              categories: data?.map((price) => price.time_close * 1000),
            },
            yaxis: {
              show: false,
            },
            fill: {
              type: 'gradient',
              gradient: { gradientToColors: ['violet'], stops: [0, 100] },
            },
            colors: ['#6c5ce7'],
            tooltip: {
              y: {
                formatter: (v) => `$ ${v.toFixed(2)}`,
              },
            },
          }}
        />
      )}
    </>
  );
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

export default Chart;
