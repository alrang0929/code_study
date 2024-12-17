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
// 기존의 redux : dispatch 안에는 액션 객체가 들어가야함 
// 그렇다면 여기서 fetchTodos()는 action creater일까? 
// fetchTodos()는 액션 객체가 아닌 청크함수를 넘겨주는 것


  return (
    <div>
      <AddForm />
      <TodoListContainer />
    </div>
  );
};

export default App;
