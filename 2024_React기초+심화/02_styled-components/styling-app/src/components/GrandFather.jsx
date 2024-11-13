import React from "react";
import Father from "./Father";
import { FamilyContext } from "../context/FamilyContext";

function GrandFather(props) {
  // 드릴링 형식의 props 전달
  //   const houseName = "스파르타";
  //   const poketMoney = 10000;
  //   return (
  //     <div>
  //       <Father houseName={houseName} poketMoney={poketMoney} />
  //     </div>
  //   );

  const houseName = "스파르타";
  const poketMoney = 10000;

  // 화면 렌더링 구역//////////////////////////////
  return (
    <>
    {/* Provider: 공유해야하는 값을 공유해주는 놈 */}
      <FamilyContext.Provider
        value={{
          houseName,
          poketMoney,
        }}
      >
        <Father />
      </FamilyContext.Provider>
      ;
    </>
  );
}

export default GrandFather;
