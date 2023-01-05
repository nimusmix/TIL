import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { useQuery } from 'react-query';
import { axiosCoins } from '../api';
import { Helmet } from 'react-helmet';
import { useSetRecoilState } from 'recoil';
import { isDarkAtom } from '../atoms';
import Btn from '../components/buttons';

function Coins() {
  const { isLoading, data } = useQuery<ICoin[]>('allCoins', axiosCoins);
  const setDarkAtom = useSetRecoilState(isDarkAtom);
  const toggleDarkAtom = () => setDarkAtom((prev: boolean) => !prev);

  return (
    <Container>
      <Helmet>
        <title>Coins</title>
      </Helmet>
      <Header>
        <Btn txt="mode" onClick={toggleDarkAtom}></Btn>
        <Title>Coins</Title>
      </Header>
      {isLoading ? (
        <Loader>Loading ...</Loader>
      ) : (
        <CoinsList>
          {data?.map((coin) => (
            <Coin key={coin.id}>
              <Link
                to={{
                  pathname: `/${coin.id}`,
                  state: { name: coin.name },
                }}
              >
                <Img src={`https://coinicons-api.vercel.app/api/icon/${coin.symbol.toLowerCase()}`} />
                {coin.name} &rarr;
              </Link>
            </Coin>
          ))}
        </CoinsList>
      )}
    </Container>
  );
}

const Container = styled.div`
  padding: 0px 20px;
  max-width: 480px;
  margin: 0 auto;
`;
const Header = styled.header`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  justify-items: center;
  align-items: center;
  height: 15vh;
`;
const CoinsList = styled.ul``;
const Coin = styled.li`
  color: ${(props) => props.theme.bgColor};
  background-color: ${(props) => props.theme.textColor};
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 10px;
  a {
    display: flex;
    align-items: center;
    transition: color 0.2s ease-in;
  }
  &:hover {
    a {
      color: ${(props) => props.theme.accentColor};
    }
  }
`;
const Title = styled.h1`
  font-size: 3rem;
  color: ${(props) => props.theme.accentColor};
`;
const Loader = styled.div`
  text-align: center;
`;
const Img = styled.img`
  width: 25px;
  height: 25px;
  margin-right: 10px;
`;

interface ICoin {
  id: string;
  name: string;
  symbol: string;
  rank: number;
  is_new: boolean;
  is_active: boolean;
  type: string;
}
export default Coins;
