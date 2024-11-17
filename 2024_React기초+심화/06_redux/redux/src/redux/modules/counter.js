// Reducer(함수) 생성

// 1. store에 들어갈 초기값을 생성한다. (useState 생성할 초기값 설정하는거랑 같은 이치)
const initialState = {
    //초기값이 꼭 객체일 필요 X
    Number: 0,
}
// 2. reducer 함수 인자 2개 받음. 사용 방법임 ㄱㄱ
// const counter = (state, action <= type이라는 값을 가지고 있는 객체 ) => {}; 
// reducer 는 무슨 함수? 변화를 일으키는 함수!
// 변화의 종류는 action.type에 담겨있음
// sotre에서 (1)어떤 변화를 일으킬건지 (2)얼만큼의 변화를 일으킬건지가 명시되어있음
const counter = (state=initialState, action) => {
    switch (action.type) {
 
        default:
            // 리듀서 함수는 항상 return문으로 끝내기
           return state;
    }
};
// 3. 내보낸다. 내보낸 놈은 생성한 store에서 받아 combine 해준다
export default counter;