// rafce < 요거 스니펫
import React from 'react'
import { StyledBox } from '../CSS/StyledBox'

const Box1 = ({initCount}) => {
    console.log("박스1이 랜더링 되었습니다!");
//코드 리턴구역////////////////////////
  return (
    <StyledBox bgcolor={"#91c49f"}>
      <button 
      // props로 전달받은 함수이므로 바로 실행할 수 없음, 따라서 화살표 함수로 실행시킴
      // 컴포넌트가 렌더링될 때마다 함수가 실행될 수 있습니다. 이는 의도하지 않은 동작을 유발하거나 성능 문제를 일으킬 수 있다. 화살표 함수를 사용하면 onClick 이벤트가 발생했을 때만 코드를 실행하도록 제어할 수 있다. 즉 화살표 함수 = 함수 실행을 지연시키는 역할
      // 컴포넌트 내부에 함수가 있을 경우 바로 참조가 가능하기 때문에 함수명 그냥 입력해도 바로 참조 할 수 있음.
      onClick={()=>{initCount()}}
      >
        초기화
      </button>
      </StyledBox>
  )
}

export default React.memo(Box1)