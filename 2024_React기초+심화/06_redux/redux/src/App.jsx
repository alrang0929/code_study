import { useSelector } from "react-redux";
import { useDispatch } from 'react-redux';
import { addNumber, removeNumber } from "./redux/modules/counter";
import { useState } from "react";
// import { minusOne, plusOne } from "./redux/modules/counter";
function App() {
  const [count, setCount] = useState(0);
  // redux를 써봅쉬다
  const counterReducer = useSelector((state)=>state.counter //초기값 설정한 객체 들어감
    );
  console.log("state",counterReducer);

  // dispatch란? 액션객체를 리듀서로 보내는 전달자 역할
  // 액션객체 type는 상수(전부 대문자)로 작성
  // 리듀서란? 디스패치를 통해 전달받은 액션객체를 검사하고, 조건이 일치하면 새로운 상태값을 만들어 내는 "변화를 만들어내는"함수

const dispatch = useDispatch(); //액션객체를 reducer에게 보내는 역할

  return (
  <>
  {counterReducer.number} 
  <br />
  <input type="number" value={count} />
  <button onClick={()=>{
    dispatch(addNumber(1));
    //onClick 이벤트 발생> reducer로 액션 객체가 날라감
  
  }}>더하기</button>
  <button onClick={()=>{
    dispatch(removeNumber(1));
    //onClick 이벤트 발생> reducer로 액션 객체가 날라감
  
  }}>빼기</button>
  </>
);
}

export default App;
