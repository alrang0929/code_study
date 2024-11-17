import React, { useState } from 'react'

const HavyComponent = () => {
  const [value,setValue] = useState(0);
  // 코드 리턴구역/////////////////////////
  return (
    <>
    <div>HavyComponent</div>
    <p>나는{value}를 가져오는 엄청 무거운 컴포넌트야</p>
    <button
    onClick={setValue(value+1)}
    >이 버튼을 누르면 count가 올라가요</button>
    <br />
    {value}
    </>
  )
}

export default HavyComponent