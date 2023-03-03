import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

const Detail = () => {
  const { id } = useParams();
  const todos = useSelector((state) => state);
  const todo = todos.find((todo) => todo.id === parseInt(id));

  return <p>{todo?.text}</p>;
};

export default Detail;
