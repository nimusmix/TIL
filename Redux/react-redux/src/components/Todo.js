import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { deleteTodo } from "../store";

const Todo = ({ text, id }) => {
  const dispatch = useDispatch();

  return (
    <li>
      <Link to={`/${id}`}>
        {text} <button onClick={() => dispatch(deleteTodo(id))}>DEL</button>
      </Link>
    </li>
  );
};

export default Todo;
