import { createStore } from "redux";

const plus = document.getElementById("plusBtn");
const minus = document.getElementById("minusBtn");
const num = document.querySelector("span");

const PLUS = "PLUS";
const MINUS = "MINUS";

const countModifier = (cnt = 0, action) => {
  switch (action.type) {
    case PLUS:
      return cnt + 1;
    case MINUS:
      return cnt - 1;
    default:
      return cnt;
  }
};

const countStore = createStore(countModifier);

const onChange = () => {
  num.innerText = countStore.getState();
};

countStore.subscribe(onChange);

plus.addEventListener("click", () => countStore.dispatch({ type: PLUS }));
minus.addEventListener("click", () => countStore.dispatch({ type: MINUS }));
