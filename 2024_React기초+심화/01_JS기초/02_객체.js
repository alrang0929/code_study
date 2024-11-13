/***************************************************************************** 

1. 객체란? key:value로 이루어진 값을 저장하는 데이터 구조 or 타입
2. JSON: (JavaScript Object Natation) : 데이터를 주고 받을 때 주로 사용하는 형식



*****************************************************************************/

const user = {
name: "르탄이",
age: "30",
isAdmin: true,
printHello: ()=> console.log("hello"),
};
// 객체에는 어떠한 데이터 타입이든 다 들어갈 수 있음!! 함수도 들어갈 수 있음!


// 객체접근 방법1. 점표기법
// console.log(user.name);
// console.log(user.age);
// user.printHello();

// 객체접근 방법2. 괄호 기법
// key값이 변수일때 주로 사용
// const attribute = "name";
// console.log(user [attribute]);


// 속성 추가
user.email = "sss@gmail.com";

// 속성변경
user.age = 31;

/* 

  name: '르탄이',
  age: 31,
  isAdmin: true,
  printHello: [Function: printHello],
  email: 'sss@gmail.com'

*/

// 속성삭제
delete user.isAdmin;
console.log(user);

/* 

{
  name: '르탄이',
  age: 31,
  printHello: [Function: printHello],
  email: 'sss@gmail.com'
}

*/

/* 
이는 객체 자체가 변경된게 아님, 불변성이 깨진 상태
*/