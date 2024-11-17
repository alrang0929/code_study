import styled from "styled-components";
import { StyledNav } from "./CSS/styled_element";
import HavyComponent from "./components/HavyComponent";

function App() {
const FooterStyle = styled.footer`
  background-color: green;
  margin-top: 30px;

`
  // 코드 리턴구역/////////////////////////
  return (
  <>
  
  <h1>useMemo</h1>
  <StyledNav bgcolor={"yellow"}> 네비게이션 바</StyledNav>
  <HavyComponent/>
  <FooterStyle> 푸터 영역 </FooterStyle>
  </>
  );
}

export default App;
