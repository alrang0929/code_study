import React, { useMemo, useState } from 'react'

const HavyComponent = () => {
  const [value,setValue] = useState(0);
  const havyWork = () => {
    // 이렇게 무거운 놈은 실행시간이 길어 다음 실행까지 오래걸림.. 따라서 캐싱처리 필요 어떻게?

    for(let i = 0 ; i<10000;i++ ){} //for
    return 100;
  }; //havyWork
  const sampleValue = useMemo(()=>havyWork(),[]); // 이렇게 캐싱, 이것도 의존성 심을 수 있음
  // 코드 리턴구역/////////////////////////
  return (
    <>
    <div>나는 {sampleValue}를 가져오는 엄청 무거운 녀석</div>
    <button
    onClick={()=>{setValue(value +1)}}
    >
      나를 누르면 count가 올라감
    </button>
    <br />
    {value}
    
    </>
  )
}

export default HavyComponent