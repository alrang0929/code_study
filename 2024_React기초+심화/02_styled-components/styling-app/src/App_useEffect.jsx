import React, { useEffect, useState } from "react";

function App(props) {
const [value, setValue] = useState("");
const [count, setCount] = useState(0);
useEffect(() => {
console.log("hello useEffect!");

// 의존성배열: 배열에 값을 넣으면 그 값이 바뀔 때만 useEffect를 실행한다
// 빈배열: 트리거가 없다? 컴포넌트가 최초 랜더링 되었을 때 딱 한번만 실행됨
},[])

  return (
    <>
    <h1>useEffect</h1>
<input 
type="text"
value={value}
// input 박스의 값이 변경되면 value에 해당되는 상태(=setValue)가 변경되며 App 컴포넌트가 리랜더링 되는 것.
// 따라서 useEffect가 다시 실행된다
// 이는 useEffect의 두번째 인자인 의존성 배열로 해결한다
onChange={(e)=>setValue(e.target.value)}
/>
<br/>
{count}
<br/>
<button
onClick={()=>{
  setCount(count+1);
}}
>
증가
</button>
    </>
  );
}

export default App;
