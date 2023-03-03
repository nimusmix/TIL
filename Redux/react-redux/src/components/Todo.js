import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { deleteTodo } from "../store";

const Todo = ({ text, id }) => {
  const dispatch = useDispatch();

  return (
    <li>
      <Link to={`/${id}`}>{text}</Link>
      <button onClick={() => dispatch(deleteTodo(id))}>DEL</button>
    </li>
  );
};

export default Todo;
