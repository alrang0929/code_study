import { useState } from "react";
import { useDispatch } from "react-redux";
import { addTodoAsync } from "../redux/slices/todos";

const AddForm = () => {
  const [title, setTitle] = useState("");
  const dispatch = useDispatch();

  const onSubmitHandler = (e) => {
    e.preventDefault();
    if (title === "") return; // 아무것도 입력하지 않았을 때 dispatch 하지 않음

    dispatch(
      addTodoAsync({
        id: new Date().getTime(),
        title,
        isDone: false,
      })
    );
    setTitle(""); // 제출 후 입력 필드 초기화
  };

  return (
    <div>
      <form onSubmit={onSubmitHandler}>
        <label>Todos의 제목을 입력하세요</label>
        <input
          type="text"
          value={title}
          onChange={(e) => {
            setTitle(e.target.value);
          }}
        />
        <button type="submit">추가하기</button>
      </form>
    </div>
  );
};

export default AddForm;
