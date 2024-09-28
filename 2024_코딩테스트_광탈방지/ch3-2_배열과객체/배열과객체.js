// 빈 배열 생성
const arr = new Array();
// or const arr = []
const arr1 = [];
const arr2 = [1, 2, 3, 4, 5];

// 빈 배열 5개 생성
const arr3 = new Array(5);

console.log("arr", arr);
console.log("arr1", arr1);
console.log("arr2", arr2);
console.log("arr3", arr3);

/*************************************** 
 ▲ 결과값
 
 arr []
 arr1 []
 arr2 [ 1, 2, 3, 4, 5 ]
 arr3 [ <5 empty items> ]
 
 ***************************************/

// 특정값으로 배열을 초기화값을 삽입할 경우
// fill(): 생성된 배열에 해당 값을 채워라
const arr4 = new Array(5).fill(5);
console.log("arr4", arr4);

// from(배열생성, function(배열의 값, idx));
const arr5 = Array.from(Array(5),function(v,i){
    // 코드는 0부터 시작하기 떄문에 보정값 1 해줌
    return i + 1;
});
console.log("arr5", arr5.length);

// length로 직접 조작도
arr5.length = 3;
console.log("arr5", arr5);

// arr5 [ 1, 2, 3 ]
// 특정 값으로 문자열을 출력해야할 경우는 join("");
console.log("arr5", arr5.join("★"));

// 거꾸로! 원본 배열도 변경되니 참고
console.log( arr5.reverse());
// [ 3, 2, 1 ]

// 합칠떄는?concat 사용!
console.log(arr1.concat(arr2));
// [ 1, 2, 3, 4, 5 ]


// 배열의 요소 추가 삭제
// push: 끝에 추가, pop : 끝에 삭제! (pop하고 터트림!)

const arr6 = [1,2,3,4,5];
arr6.push("999");

console.log(arr6);
//push 결과값: [ 1, 2, 3, 4, 5, '999' ]

arr6.pop();
console.log(arr6);
// [ 1, 2, 3, 4, 5 ]

// 첫번째 요소 삭제 : shift, 첫번쨰 요소 추가: unshift
// 전에 메뉴 맨 앞에 뭐 추가할 떄 사용했었음
arr6.shift();
console.log(arr6);

arr6.unshift(8888);
console.log(arr6);
// [ 8888, 2, 3, 4, 5 ]

// 2번재 배열~ 4번쨰 배열만 가져오고 싶으면?
console.log(arr6.slice(1,4));
// 결과값: [ 2, 3, 4 ]

/********************************************8 

원본배열에 영향을 주는 놈들:
pop, push, unshift, shift

안주는 놈들:
slice, splice

*******************************************8*/

// 특정 위치의 값을 지우고 싶으면?
// splice(시작점, 몇개);
arr6.splice(2,1);
console.log(arr6);
// 원본: [ 8888, 2, 3, 4, 5 ]
//결과값: [ 8888, 2, 4, 5 ]


// 배열의 순회

const arr7 = [1,2,3,4,5,6,7,8,9,10];

for( let i = 0 ; i < 10 ; i += 1 ){
    console.log(arr7[i])
}
//10번 배열까지 순회 끝

// for of
for(const item of arr7){
    console.log(item);
}

// 이렇게 돌아도 값은 동일함
// 직관적이여서 ㅊㅊ

console.log(typeof arr7);
// object
