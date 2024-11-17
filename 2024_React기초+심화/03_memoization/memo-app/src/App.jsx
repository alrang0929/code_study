import { useCallback, useState } from "react";
import styled from "styled-components";
import Box1 from "./components/Box1";
import Box3 from "./components/Box3";
import Box2 from "./components/Box2";

const StyleBoxList = styled.div`
  display: flex;
  margin-top: 10px;
`;
function App() {
  console.log("App 컨포넌트가 랜더링 되었습니다!");
  const [count, setCont] = useState(0);
  // App 컴포넌트가 리랜더링 되면 initCount함수를 props 받아 사용하고 있는 Box1도 리렌더링됨. 왜? ★함수형 컴포넌트★를 사용하기 때문!
  // 리랜더링 되면서 initCount가 참조하고 있던 주소도 변경됨
  // 따라서 Box1의 불필요한 랜더링을 막기 위해 initCount를 메모이제이션 해야됨.
  const initCount = useCallback(() => {
    console.log(`[count변경] ${count}에서 0으로 변경되었습니다`) //[count변경] 0에서 0으로 변경되었습니다
    // 왜? initCount 렌더링 되는 시점 = App 컴포넌트가 최초 렌더링 됐을때. 즉 count가 0 일 때, 따라서 initCount는 영원히 0
    // 만약 count를 반영하고 싶다면 의존성에 count 추가

    setCont(0);
  },[count]); // [](dependency array) : 의존성!! useCallback도 의존성을 부여할 수 있다

  const plusButtonHandler = () => {
    setCont(count + 1);
  };
  const minusButtonHandler = () => {
    setCont(count - 1);
  };
  // 코드 리턴구역////////////////////
  return (
    <>
      <h1>카운트 예제입니다</h1>
      <p>현재 카운트: {count} </p>
      <button onClick={plusButtonHandler}>+</button>
      <button onClick={minusButtonHandler}>-</button>
      <StyleBoxList>
        <Box1 initCount={initCount} />
        <Box2 />
        <Box3 />
      </StyleBoxList>
    </>
  );
}

export default App;
