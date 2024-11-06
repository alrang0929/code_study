// const fruits = ["Apple","Banana"];
// [ 'Apple', 'Banana' ]
// console.log(fruits);

// orange를 추가해보자 아.. push: 뒤에 추가
// fruits.unshift("Orange");
// fruits.push("Orange");
// console.log(fruits);

// fruits.pop("Orange");
// console.log(fruits);

// const lastFruit = fruits.pop();
// console.log("=============================");
// console.log(lastFruits);
// console.log(fruits);

/* 

pop : 마지막 요소를 pop 하고 터트림!! 

[ 'Apple', 'Banana', 'Orange' ]
=============================
Orange
[ 'Apple', 'Banana' ]

*/

// map: 원본 배열을 가공한 "새로운" 배열을 return 하는 함수
// 1) 배열 내의 모든 요소 각각에 대해
// 2) 주어진 함수를 호출한 결과를 모아
// 3) 새로운 배열을 반환 한다.

// const numbers = [1,2,3,4,5];
// const squared = numbers.map(주어진 함수);
// const squared = numbers.map(function(num){
//     return num * num;
// });

// 예상결과 [1,4,9,16,25]
// console.log(squared);
// 결과: [ 1, 4, 9, 16, 25 ]

/* 
유튜브를 예시로 들때 database가 어떻게 되어있을까?
테이블 형태로 배치되어있음
1) 브라우저에서 데이터를 송신 받으면
<<중간에 그 데이터를 가공해야하는 과정이 필요! 이것이 map의 역할 + 검색창을 통한 filter>>
2) 박스에 데이터를 담아 구성
*/

// filter : 주어진 함수의 테스트를 통과한 모든 요소를 새로운 배열로 만듦

// const numbers = [1, 2, 3, 4, 5];
// const evenNumbers = numbers.filter(function (num) {
//   if (num % 2 === 0) return num;
// });

// console.log(evenNumbers);
//결과: [ 2, 4 ]

// react에서 많이 쓰이는 예시
// const 동영상리스트 = [
//   {
//     idx: 1,
//     제목: "동영상 01",
//     썸네일이미지: "image01.jpg",
//   },
//   {
//     idx: 2,
//     제목: "동영상 02",
//     썸네일이미지: "image02.jpg",
//   },
//   {
//     idx: 3,
//     제목: "동영상 03",
//     썸네일이미지: "image03.jpg",
//   },
//   {
//     idx: 4,
//     제목: "동영상 02",
//     썸네일이미지: "image04.jpg",
//   },
// ];

// const 필터링된동영상리스트 = 동영상리스트.filter(function(영상){
//     return 영상.제목 === "동영상 02";
// });

// console.log(필터링된동영상리스트);
/* 
결과: 

[
  { idx: 2, '제목': '동영상 02', '썸네일이미지': 'image02.jpg' },
  { idx: 4, '제목': '동영상 02', '썸네일이미지': 'image04.jpg' }
]
*/

// reduce : 배열의 각 요소에 대해 주어진 함수를 실행하고 누적된 값을 반환하는 것(그래서 누적기라고도 함)
// const numbers = [1,2,3,4,5];
// // numbers.reduce(function(누적된값, 일반값){});
// const  result = numbers.reduce(function(누적된값, 일반값){
// console.log("===========================================");
// console.log("누적된값",누적된값);
// console.log("일반값",일반값);


/* 
===========================================
누적된값 1
일반값 2
===========================================
누적된값 undefined
일반값 3
===========================================
누적된값 undefined
일반값 4
===========================================
누적된값 undefined
일반값 5

누적된 값이 두번째 값 부터 undefined가 들어감

*/


// return에 조건을 추가
// return 누적된값+일반값;

/* 

===========================================
누적된값 1
일반값 2
===========================================
누적된값 3
일반값 3
===========================================
누적된값 6
일반값 4
===========================================
누적된값 10
일반값 5

누적된 값: return(= 누적된값+일반값)의 값
일반값: 누적된 값으로 들어가는 다음 값

점점 쌓여감..

*/

// });

// console.log("result =>", result);
// result => 15





// sort 정렬: 원본배열 값 자체를 바꿔버림. 비교함수를 넣지 않으면 유니코드를 기반으로 비교를 하여 정렬함
// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// console.log(fruits);
// console.log(fruits.sort());

/* 
[ 'Banana', 'Orange', 'Apple', 'Mango' ]
[ 'Apple', 'Banana', 'Mango', 'Orange' ]
*/

const numbers = [40,100,1,5,25];
console.log(numbers);
numbers.sort((a,b)=> a - b);
// a-b : 오름차순, b-a: 내림차순
console.log(numbers);

/*
결과:
[ 40, 100, 1, 5, 25 ]
[ 1, 5, 25, 40, 100 ]
*/