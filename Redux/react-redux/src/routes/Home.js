import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addTodo } from "../store";
import Todo from "../components/Todo";

const Home = () => {
  const todos = useSelector((state) => state);
  const dispatch = useDispatch();
  const [text, setText] = useState("");
  const onChange = (e) => {
    setText(e.target.value);
  };
  const onSubmit = (e) => {
    e.preventDefault();
    dispatch(addTodo(text));
    setText("");
  };

  return (
    <>
      <h1>TODO</h1>
      <form onSubmit={onSubmit}>
        <input type="text" value={text} onChange={onChange} />
        <button>ADD</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <Todo {...todo} key={todo.id} />
        ))}
      </ul>
    </>
  );
};

export default Home;
