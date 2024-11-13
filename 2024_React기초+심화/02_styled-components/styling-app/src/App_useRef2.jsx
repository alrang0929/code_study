import React, { useRef, useState } from "react";

function App(props) {
  const [count, setCount] = useState(0);
  const countRef = useRef(0);

  const plusStateCountButtonHandler = () => {
    setCount(count + 1);
  };
  const plusRefCountButtonHandler = () => {
    countRef.current++;
  };
  return (
    <>
      <h1>useREf VS useState</h1>
      <div className="state">
        <span>state 영역입니다{count}</span>
        <br />
        <button
          onClick={plusStateCountButtonHandler}
        >
          state 증가
        </button>
      </div>
      <br />
      <div className="Ref">
        <span>ref 영역입니다</span>{countRef.current}
        <br />
        <button
        onClick={plusRefCountButtonHandler}
        >
          ref 증가
        </button>
      </div>
      <br />
    </>
  );
}

export default App;
