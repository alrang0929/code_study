/*********************************** 

JS에서 배열 사용하는 방법

push(): 배열의 끝에 추가하는 메서드

splice(): 배열의 중간에 추가/제거 가능

1. 빈 배열을 생성
2. 미리 초기화된 배열 생성
3. 같은 값으로 초기화된 배열 생성
4. 로직을 사용하여 생성

***********************************/

const arr = [1, 2, 3];

console.log("초기배열",arr);
// push를 사용하여 배열 끝에 4 추가
arr.push(4);
console.log("push",arr);


/* 

array.splice() 사용법

array.splice(start, deleteCount, item1, item2, ...);

(시작점, 삭제할 수, 추가할 것1, 추가할 것2, 추가할 것3,)
*/
arr.splice(3,0,128);
// idx 3번 자리에 128을 추가해라
console.log("splice",arr);
// 결과: splice [ 1, 2, 3, 128, 4 ]

arr.splice(2,0,99999);
console.log("splice2",arr);
// 결과: splice2 [ 1, 2, 99999, 3, 128, 4 ]

// 값을 제거할떄 splice
// arr.splice(0,1);
// console.log("splice 제거1",arr);

// arr.splice(0,3);
// console.log("splice 제거2",arr);

// 제거시 splice(위치,갯수);
arr.splice(3,2);
console.log("splice 제거3",arr);
// 결과: splice 제거3 [ 1, 2, 99999, 4 ]

////////////////////////////////////////////
// JS 배열의 특징: 숫자값 뿐만 아니라 문자값, 논리값(true / false)도 들어갈 수 있음!
// ㄴ> 근본적으로 js 배열은 객체이기 떄문!
// 예시
const arr1 = [];
console.log("초기값 arr1", arr1);
arr1.push(1);
arr1.push(1);
arr1.push(2);
arr1.push(3);

console.log("push 반영",arr1);
// 결과: push 반영 [ 1, 1, 2, 3 ]

arr["배고파잉"] = 10;
arr[false] = true;
console.log("문자, 논리값이 반영되는 arr", arr1);
// 문자, 논리값이 반영되는 arr [ 1, 1, 2, 3 ]
console.log("배열의 갯수는?", arr1.length);
// 배열의 갯수는?? 4

arr1[2] = "홀롤ㄹ로";
console.log(arr1);
// [ 1, 1, '홀롤ㄹ로', 3 ]
console.log("배열의 갯수는?2", arr1.length);
// 배열의 갯수는?2 4 = 문자형도 배열로 인식!








