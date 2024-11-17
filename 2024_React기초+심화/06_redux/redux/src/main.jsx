import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import { Provider } from "react-redux";
import App from "./App.jsx";
import store from "./redux/config/configStore.js";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    {/* 
    1. Provider 로 컴포넌트들을 감쌈 (이때 react-redux provider인지 확인)
    2. 내보내기한 store를 받는다.

    
    */}
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>
);
