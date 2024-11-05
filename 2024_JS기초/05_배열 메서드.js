const fruits = ["Apple","Banana"];
// [ 'Apple', 'Banana' ]
// console.log(fruits);

// orange를 추가해보자 아.. push: 뒤에 추가
// fruits.unshift("Orange");
fruits.push("Orange");
// console.log(fruits);

// fruits.pop("Orange");
console.log(fruits);

const lastFruits = fruits.pop();
console.log("=============================");
console.log(lastFruits);
console.log(fruits);

/* 

pop : 마지막 요소를 pop 하고 터트림!! 

[ 'Apple', 'Banana', 'Orange' ]
=============================
Orange
[ 'Apple', 'Banana' ]

*/