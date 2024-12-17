import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// 비동기 작업을 위한 thunk 액션 생성
export const fetchTodos = createAsyncThunk("todos/fetchTodos", async () => {
  const response = await axios.get("http://localhost:4000/todos");
  return response.data;
});
// createAsyncThunk를 통해 호출된 결과물을 담고있음 

// 1. createAsyncThunk을 통해 처리된 이름을 부여
export const addTodoAsync = createAsyncThunk("todos/addTodo", async (todo) => {
  // 2. 비동기 함수에 대한 내용을 처리를 하고 그 내용을 가지고 그 내부의 스토어에 값을 전달하기 위한 것
  const response = await axios.post("http://localhost:4000/todos", todo);
  // 리턴된 값이 적달되는 것것
  return response.data;
});

export const deleteTodoAsync = createAsyncThunk(
  "todos/deleteTodo",
  async (id) => {
    await axios.delete(`http://localhost:4000/todos/${id}`);
    return id;
  }
);

export const toggleTodoAsync = createAsyncThunk(
  "todos/toggleTodo",
  async (todo) => {
    const response = await axios.patch(
      `http://localhost:4000/todos/${todo.id}`,
      {
        isDone: !todo.isDone,
      }
    );
    return response.data;
  }
);

const todosSlice = createSlice({
  name: "todos",
  initialState: {
    todos: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTodos.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        state.loading = false;
        state.todos = action.payload;
      })
      .addCase(fetchTodos.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })
      .addCase(addTodoAsync.fulfilled, (state, action) => {
        state.todos.push(action.payload);
      })
      .addCase(deleteTodoAsync.fulfilled, (state, action) => {
        state.todos = state.todos.filter((todo) => todo.id !== action.payload);
      })
      .addCase(toggleTodoAsync.fulfilled, (state, action) => {
        state.todos = state.todos.map((todo) =>
          todo.id === action.payload.id ? action.payload : todo
        );
      });
  },
});

export default todosSlice.reducer;
