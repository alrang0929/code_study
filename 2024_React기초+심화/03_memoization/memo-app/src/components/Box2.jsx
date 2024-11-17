
import React from 'react'
import { StyledBox } from '../CSS/StyledBox'
const Box2 = () => {
    console.log("박스2이 랜더링 되었습니다!");
    //코드 리턴구역////////////////////////
  return (
    <StyledBox bgcolor={"skyblue"}>Box2</StyledBox >
  )
}

export default React.memo(Box2)