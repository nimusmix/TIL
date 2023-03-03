import { configureStore, createAction, createReducer } from "@reduxjs/toolkit";

export const addTodo = createAction("ADD");
export const deleteTodo = createAction("DEL");

const reducer = createReducer([], {
  [addTodo]: (state, action) => {
    state.push({ text: action.payload, id: Date.now() });
  },
  [deleteTodo]: (state, action) => {
    return state.filter((todo) => todo.id !== action.payload);
  },
});

const store = configureStore({ reducer });

export default store;
