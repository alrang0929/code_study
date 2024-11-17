// 배열 Destructuring  문제

/* 
문제1

다음 자바스크립트 객체에서 name과 age를 디스트럭처링을 사용하여 추출하고 출력하는 코드를 작성하세요.

*/

const person = {
  name: "르탄이",
  age: 25,
  job: "개발자",
};

console.log(
  `안녕하세요 저는 ${person.name}입니다. 나이는 ${person.age}살 입니다.`
);
//안녕하세요 저는 르탄이입니다. 나이는 25살 입니다.

/* 
문제2

다음 자바스크립트 객체에서 title과 year를 디스트럭처링을 사용하여 추출하고 출력하는 코드를 작성하세요.

*/
const movie = {
  title: "Inception",
  director: "Christopher Nolan",
  release: {
    year: 2010,
    month: "July",
  },
};

const {title, release:{year}} = movie;
console.log(title, year);

/* 
  문제 3

  다음 자바스크립트 배열에서 첫 번째와 세 번째 요소를 디스트럭처링을 사용하여 추출하여 first, third 변수에 담아 출력하는 코드를 작성하세요.
  
  */

const numbers = [10, 20, 30, 40, 50];
const [first, , third] = numbers;
console.log(first, third);

/* 
문제4

호텔의 예약 확인 시스템의 함수라고 가정합니다. 아래 결과와 같이 출력되도록 함수를 완성해 보세요.
*/

function confirmReservation({name,roomType, date: firstDate}) {
    // 여기에 user 객체를 구조 분해 할당 하세요.
    
    return `${name} 고객님의 ${roomType}룸 입실날짜는 ${firstDate} 입니다.`
}

const userInfo = {
name: "James",
roomType: "Deluxe",
date: "2023-05-30"
}
// const result = confirmReservation(userInfo);
// console.log(result);

/**************************************************************

Spread Operator 문제

- 다음 두 배열 `array1`과 `array2`가 주어졌을 때, 두 배열을 합친 새 배열 `combinedArray`를 스프레드 연산자를 사용하여 만들고, 결과를 출력하는 코드를 작성하세요.
- 또한, `array1`을 스프레드 연산자를 사용하여 복제한 후 원본 배열 `array1`에 변화를 주어 복제된 배열이 영향을 받지 않는지 검증하는 코드도 작성하세요.

**************************************************************/

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combinedArray = [...array1, ...array2];

// console.log(combinedArray); //[ 1, 2, 3, 4, 5, 6 ] 정답! :D
// 원본배열은?
const copyArray1 = [...array1];
// console.log(copyArray1); //[ 1, 2, 3 ]

/* 

다음 두 객체 `obj1`과 `obj2`가 주어졌을 때, 두 객체의 속성을 스프레드 연산자를 사용하여 병합한 새 객체 `mergedObj`를 생성하고 결과를 출력하세요.

단, 같은 이름의 키가 존재할 경우 `obj2`의 값이 우선하여 반영되어야 합니다. 또한, `mergedObj`에서 `name` 속성의 값을 **'원장님'**으로 변경 후, 원본 객체 `obj1`과 `obj2`가 변경되지 않는 것을 확인하세요.

*/
const obj1 = { name: "르탄이", age: 25 };
const obj2 = { name: "르순이", email: "rsoony@sparta.com" };

const mergedObj = { ...obj1, ...obj2 };
mergedObj.name = "원장님";

// console.log(mergedObj);
// console.log("obj1=>",obj1,"obj2=>",obj2);

/* 

{ name: '원장님', age: 25, email: 'rsoony@sparta.com' }
obj1=> { name: '르탄이', age: 25 } obj2=> { name: '르순이', email: 'rsoony@sparta.com' }

맞춘듯?

*/
// rest operator이 언제 쓰이냐?
// 1)함수의 매계변수
/* function sum(...numbers){
    console.log("here!",numbers)
    return numbers.reduce((acc, cur) => acc + cur)
};
const result = sum(1,2,3,4,5); */

// 2)객체 분해 할당 시, 여러값을 그룹핑
const person2 = {
name: 'John',
age:30,
country: "USA",
occupation: "Developer",
}

// 기존의 객체구조분해할당
// const {name, age, country,occupation} = person2;
//  {버릴놈, 묶을놈} = 대상 객체 ;
const {occupation,...rest} = person2;
console.log("rest=>",rest);

/* 

[rest operator 문제]
person 객체에서 password를 제외한 나머지 요소를 sampleObj 변수에 담아 분리해보세요.
*/

// const person = { name: 'Young', age: 35, job: "developer", password: "1234" }

// 여기에 코드를 작성합니다.

// const sampleObj = delete person.password;

// console.log(sampleObj) // => { name: 'Young', age: 35, job: "developer" }
