// 객체생성
const obj1 = new Object();
const obj2 = {};
const obj3 = {name: "김철수", age: 28, company:"cobit"};

console.log(obj1);
console.log(obj2);
console.log(obj3);

/************************************************ 

결과값: 
{}
{}
{ name: '김철수', age: 28, company: 'cobit' }

************************************************/


// 객체를 추가하려면?
// 1. key값 = value로 추가
obj1["email"] = "aaa@aaaaa.com";
console.log(obj1);
/* 
결과값:

{ name: '김철수', age: 28, company: 'cobit' }
{ email: 'aaa@aaaaa.com' }
*/
// 그 뭐야... map 돌릴떄 . 으로 찾아 들어가는 거랑 같은 맥락일려나?
obj1.hobby = "game";
console.log(obj1);

/* 
결과값:

{ name: '김철수', age: 28, company: 'cobit' }
{ email: 'aaa@aaaaa.com' }
{ email: 'aaa@aaaaa.com', hobby: 'game' }

*/

// 객체 요소를 삭제하려면? delet 사용! //////////////
delete obj1.hobby;
console.log("delete값",obj1);
/* 
결과:
{ email: 'aaa@aaaaa.com' }
*/

// in 오퍼레이터를 활용한 key값 유무 확인
//  요소가 있냐? 배열안에 = 논리값으로 반환
console.log("hobby" in obj1);//false
console.log("email" in obj1);//true

// 키값을 알아오고 싶냐? Object.keys(객체);
console.log(Object.keys(obj1));
//결과값: [ 'email' ]

// value값을 알아오고 싶냐? Object.values(obj1)
console.log(Object.values(obj1));
//결과값: [ 'aaa@aaaaa.com' ]

// for in을 사용한 객체 순회
for(const key in obj1){
    console.log(key, obj1[key]);
}
// 결과값: email aaa@aaaaa.com