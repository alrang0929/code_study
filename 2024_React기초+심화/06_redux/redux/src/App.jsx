// import { useSelector } from "react-redux";

function App() {
  // redux를 써봅쉬다
  // const counterReducer = useSelector((state)=>{
  //   return state.counter //초기값 설정한 객체 들어감
  //   });
  // console.log("state",counterReducer);

const dispatch = useDispatch();

  return (
  <>
  <button>+1</button>
  </>
);
}

export default App;
