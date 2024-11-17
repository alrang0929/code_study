// 중앙 상태 관리소 store
import {combineReducers, createStore} from "redux";
import counter from "../modules/counter";
// 1)roodReducer 생성
// Reducer: state 관리를 하기 위한 로직들의 집합
const rootReducer = combineReducers({
    // 생성한 모듈을 여기서 combin ㄱㄱ
    counter: counter,
}); //객체구조분해할당에는 추후 제잦ㄱ할 modules가 들어가면 됨
// 2) store 조합 : 1번에서 만든 rootReducer을 인자로 넣어줌
const store = createStore(rootReducer);
// 3) 만든 store 출력
export default store;