
import React from 'react'
import { StyledBox } from '../CSS/StyledBox'
const Box3 = () => {
    console.log("박스3이 랜더링 되었습니다!");
    //코드 리턴구역////////////////////////
  return (
    <StyledBox bgcolor={"red"}>Box3</StyledBox>
  )
}

export default React.memo(Box3)