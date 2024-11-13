import React, { useRef, useState } from 'react'

export default function App (){
const [count,setCount] = useState(0);
const ref = useRef("초기값");
console.log("ref",ref);
// {current: '초기값'}
// useState 와 useRef의 가장 큰 차이: 렌더링과 연관이 있느냐 없느냐
ref.current = "바뀐값";
console.log("current",ref);
  return (
    <>
    <h1>useRef</h1>
    <br/>
    {count}
    <br/>
    <button
    onClick={()=>{setCount(count+1)}}
    >
      증가
    </button>
    </>
  )
}
