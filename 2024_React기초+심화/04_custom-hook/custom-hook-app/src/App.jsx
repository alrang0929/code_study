import { useState } from "react";

function App() {

  const [title, onChangeTitleHandler] = useInput(); //useInput에서  return [value, handler] 에 들어가는 것들
  const [body, onChangeBodyHandler] = useInput();
  // custom hook : 커스텀한 hook
  // 상황: 동일한 절차들이 계속 반복됨.. 귀찮음 더 컴펙트하게 만들 수 없을까? > 그때 필요한게 커스텀 훅
  /************************************************** 
★custom hook을 만들 때 주의사항

1) custom hook의 함수 이름은 use로 시작하는 것이 좋다.
2) 파일 이름은 원하는 대로 편의상 useInput
3) 확장자는 js

**************************************************/
  // 화면 리턴구역/////////////////////////////////////
  return (
    <>
      <input
        type="text"
        name="title"
        value={title}
        onChange={onChangeTitleHandler}
      />
      <input
        type="text"
        name="body"
        value={body}
        onChange={onChangeBodyHandler}
      />
    </>
  );
}

export default App;
