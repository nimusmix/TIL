import { useState } from 'react'

function App() {
  const [todo, setTodo] = useState('')
  const [todos, setTodos] = useState([])

  const onChange = (event) => {setTodo(event.target.value)}
  const onSubmit = (event) => {
    event.preventDefault()
    if (!todo) {
      return
    }
    setTodos((currentTodos) => [todo, ...currentTodos])
    setTodo('')
  }

  return (
    <div>
      <h1>Todo List ({todos.length})</h1>

      <form onSubmit={onSubmit}>
        <input
          value={todo}
          onChange={onChange}
          type="text"
          placeholder="Write your to do."
        />
        <button>Add</button>
      </form>

      <hr/>
      <ul>
        {todos.map((item, idx) => <li key={idx}>{item}</li>)}
      </ul>
    </div>
  );
}

export default App;
