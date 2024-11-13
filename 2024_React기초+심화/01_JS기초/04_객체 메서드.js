// 1. 객체
// Object.keys()
const user = {
    name: "르탄이",
    age: "30",
    isAdmin: true,
  }
  
// 1)  const keys = Object.keys(user);
//   console.log(keys);
//   [ 'name', 'age', 'isAdmin' ]

const values = Object.values(user);
// 2)  console.log(values);
//   [ '르탄이', '30', true ]

// 3. entries : key와 value를 쌍으로 하는 "배열"로 반환
const entries = Object.entries(user);
//   console.log(entries);
//   [ [ 'name', '르탄이' ], [ 'age', '30' ], [ 'isAdmin', true ] ]

// 4) assign: 원본 객체에 추가할 객체를 복사
const userDetail = {
    occupation: "개발자",
};
//Object.assign(원본 객체(=데싱겍체), 합칠 녀석(=출처 객체)) 
Object.assign(user, userDetail);
  console.log(user);
//  결과값에 occupation: "개발자"가 추가된 것을 확인할 수 있음
// { name: '르탄이', age: '30', isAdmin: true, occupation: '개발자' }
