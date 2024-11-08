import React, { useEffect, useRef } from 'react';

function App(props) {
  const idRef = useRef("");
  //화면렌더링 구역
  useEffect(() => {
 idRef.current.focus();
  }, [])
  
  return (
    <>
    <div>
      아이디 : <input type="text" ref={idRef}/>
    </div>
    <div>
      비밀번호 : <input type="password" />
    </div>
    
    
    
    </>
  );
}

export default App;