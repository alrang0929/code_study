// //1. template literals///////////////////////////////////////////////
// // :변수의 표현식을 문자열 안에 쉽게 삽입할 수 있게 해주는 문법
const customer = {
  name: "르탄이",
};
const item = {
  name: "커피",
  price: 4000,
};

// console.log("감사합니다." + customer.name + "님"
// +item.name + "을" + item.price + "에 구매하셨습니다");
// // >> 감사합니다. 르탄이님, 커피을4000원에 구매하셨습니다

console.log(`감사합니다. ${customer.name}님, ${item.name}을 ${item.price}원에 구매하셨습니다.`);
// // 감사합니다. 르탄이님, 커피을 4000원에 구매하셨습니다.

// // 문자열을 여러줄로 작성하는 경우
// const oderDetails = "고객:"+customer.name + "\n" + "상품:"+item.name;
// console.log(oderDetails);
// /* 
// 고객:르탄이
// 상품:커피
// */

const oderDetails2 = `
고객: ${customer.name};
상품: ${item.name};
가격: ${item.price};
`;

// console.log(oderDetails2);
/* 
고객: 르탄이;
상품: 커피;
가격: 4000;
*/

// const item = {
//     name:"커피",
//     price: 4000,
// }
// const name = item.name;
// const price = item.price;

//구조분해할당
// const {name, price} = item;


// console.log("name:",name);
// console.log("price:",price);
/* 
name: 커피
price: 4000
*/


//2. destructuring//////////////////////////////////////////////////
function greet ({name, age}){
    console.log(`안녕하세요, 제 이름은 ${name}입니다. 나이는 ${age}에요`);
    }
    
    const person = {
    name : "르순이",
    age: 28,
    };
    

    // 2. 배열의 디스트럭 처리: 순서가 중요!!
    // 배열은 index를 key로 가짐, 요소의 위치를 기반으로 변수할당

    const colors =["red","green","blue"];
    const [firstColor, secondColor] = colors;
    const [, , thirdColor] = colors;

    // console.log(firstColor); // red
    // console.log(secondColor); // green 
    // console.log(thirdColor); // blue


