import React from "react";

// rafc
export const Child = ({ setCount }) => {
  return (
    <>
      <h3>여기는 자식 컴포넌트 입니다</h3>
      <button
        // 걍 썻다가 무한증가 해버림..ㅇㅅㅇ;;;
        onClick={() => {
          setCount((prev) => prev + 1);
        }}
      >
        증가
      </button>
    </>
  );
};
