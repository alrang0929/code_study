// src/App.js

import React from "react";
// styled-components에서 styled 라는 키워드를 import 합니다.
import styled from "styled-components";

// 1. 스타일이 적용된 컴포넌트
// const 컴포넌트명 = styled.스타일을 적용할 요소``
const StBox = styled.div`
  width: 100px;
  height: 100px;
  /* 이런식으로 조건부 스타일링 가능 */
  border: 4px solid ${(props) => props.borderColor};
  margin: 20px;
`; //stBox

const boxList = ["red", "green", "blue"];
// 박스 컬러가 변경될 때 박스 이름도 변경되야하므로 아래 함수 선언
const getBoxName = (color) => {
  switch (color) {
    case "red":
      return "빨간";
    case "green":
      return "초록";
    case "blue":
      return "파란";
      default: return "검정";
  } //switch
}; //getBoxName

function App() {
  // 화면리턴구역////////////////////////////////
  return (
    <>
      {/* 반복이 된다? react를 사용하는 이상 용서할 수 없음 */}
      {/* <StBox borderColor="red">빨간 박스</StBox>
  <StBox borderColor="green">초록 박스</StBox>
  <StBox borderColor="blue">파란 박스</StBox> */}

  {
    boxList.map((boxcolor)=>
     <StBox
    key={boxcolor}
    borderColor = {boxcolor} >{getBoxName(boxcolor)} 박스</StBox>
    )
  }
    </>
  );
} //app
export default App;
