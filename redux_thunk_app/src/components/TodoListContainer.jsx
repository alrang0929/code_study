import { useDispatch, useSelector } from "react-redux";
import { deleteTodoAsync, toggleTodoAsync } from "../redux/slices/todos";

const TodoListContainer = () => {
  const dispatch = useDispatch();
  const todos = useSelector((state) => state.todos.todos);

  const handleDelete = (id) => {
    dispatch(deleteTodoAsync(id));
  };

  const handleToggle = (todo) => {
    dispatch(toggleTodoAsync(todo));
  };

  return (
    <div>
      {todos.map((todo) => (
        <div key={todo.id}>
          <span
            style={{ textDecoration: todo.isDone ? "line-through" : "none" }}
          >
            {todo.title}
          </span>
          <button onClick={() => handleToggle(todo)}>
            {todo.isDone ? "Undo" : "Complete"}
          </button>
          <button onClick={() => handleDelete(todo.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default TodoListContainer;
