import React, { useContext } from "react";
import { FamilyContext } from "../context/FamilyContext";

function Child() {
  const {houseName, poketMoney} = useContext(FamilyContext);
  const stressesWorld = {
    color: "red",
    fontweight: 900,
  };
  return (
    <div>
      나는 이 집안의 막내에여,
      <br />
      할아버지가 우리집 이름은 <span style={stressesWorld}>{houseName}</span>
      라고 하셨어여
      <br />
      게다가 용돈도 <span style={stressesWorld}>{poketMoney}</span> 만큼
      주셨답니당
    </div>
  );
}

export default Child;
