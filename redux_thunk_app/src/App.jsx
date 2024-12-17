import { useEffect } from "react";
import { useDispatch } from "react-redux";
import TodoListContainer from "./components/TodoListContainer";
import AddForm from "./components/AddForm";
import { fetchTodos } from "./redux/slices/todos"; // 비동기 액션 가져오기

const App = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    // 컴포넌트 마운트 시 todos를 가져오는 비동기 액션 디스패치
    dispatch(fetchTodos());
  }, [dispatch]);

  return (
    <div>
      <AddForm />
      <TodoListContainer />
    </div>
  );
};

export default App;
