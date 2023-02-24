import { useParams } from "react-router-dom";

const Detail = () => {
  const { id } = useParams();
  return <p>Detail</p>;
};

export default Detail;
