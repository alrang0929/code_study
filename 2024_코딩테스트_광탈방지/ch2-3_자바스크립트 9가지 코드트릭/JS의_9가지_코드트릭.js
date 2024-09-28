/**************************************** 

JS의 9가지 코드트릭

****************************************/

// 1. 구조 분해 할당을 이용한 swap
// ES6의 구조 분해 할당 문법을 이용하여 두 변수를 swap 가능
let a =5, b=10;
[a,b] = [b,a];
console.log(a,b); // ㅁ = 10, b = 5
console.log("swap 구조분해할당 끝")

// 2. 배열 생성으로 루프 제거
// 단순히 범위 루프를 돌고 싶을때 사용

// 5와 10 까지 돌고 싶음!
// for문 오랜만이라.. 다시 정리해보자! 
// for( let i = i의 초기값 ; i를 어디까지 반복할건데 ; i는 이만큼씩 증가해!){일해라};

let sum = 0;
for( let i = 5 ; i < 10 ; i +=1 ){
    sum += i;
    /***************************** 
     sum의 초기값 = 0
    
    [1]
    0+5 = 5

    [2]
    i = 5
    5+6 = 11
    
    [3]
    1= 11
    11 + 7 = 18

    [4]
    i=18
    18+8 = 26

    [5]
    i=26
    26+9 = 35

    *****************************/
}//for

// 최종 결과값 담김
console.log(sum);
console.log("범위 지정 루프");


//3. 배열 내 같은 요소 제거 = set 사용!!
// 전에 카테고리에서 사용했었징!

const names = ["둘리","또치","고길동","희동이","희동이"];

// 먼저 Set 객체를 생성하여 names 요소를 추가
//  Array.from(...) : 생성된 배열을 다시 배열로 반환
const filterNames = Array.from(new Set(names));
// 마찬가지로 SEt객체를 생성해 중복 제거
// 스프레드 연산자를 사용하여 Set의 요소들을 새로운 배열로 확장
const filteredNames = [...new Set(names)];
console.log("filterNames", filterNames, "\n filteredNames" ,filteredNames);


//4. Spread 연산자 (...)를 이용한 객체 변합

const person1 = {
    name: "김철수",
    familyName : "김",
    givenName: "철수",
};

const company = {
    name:"cobit. inc.",
    address: "seoul"
};

const kimChulShu = {...person1, ...company};

console.log(kimChulShu);
/****************************************** 
 
결과:
{
  name: 'cobit. inc.',
  familyName: '김',
  givenName: '철수',
  address: 'seoul'
}

******************************************/


// 5. &&과 ||의 활용
// && = and, || = or

const name = "김철수" || "Guest";
// flag가 true 일 경우만 실행
// flag && func();


// &&은 객체 병합이도 사용
const makeName = (showFirstName) =>{
 return{
    name: "챠챠",
    ...showFirstName && {firstName: "김"}
 }
}//makeName

console.log(makeName(false));
// 결과: { name: '챠챠' }

console.log(makeName(true));
//  결과: { name: '챠챠', firstName: '김' }

// 6. 구조분해할당 사용하기
// 리액트의 props  활용할 때 생각하면 될듯

const person = {
    name: 'Lee Sun-Hyoup',
    familyName: 'Lee',
    givenName: 'Sun-Hyoup',
    company: 'Cobalt. Inc.',
    address: 'Seoul',
}
const {givenName, address} = person;


/************************************************* 
 

객체 구조분해 할당을 하면 원본은 보존됨, 따라서
console.log(person) 을 해도 기존 값인

{
    name: 'Lee Sun-Hyoup',
    familyName: 'Lee',
    givenName: 'Sun-Hyoup',
    company: 'Cobalt. Inc.',
    address: 'Seoul',
}

가 콘솔에 찍힘!

따라서 객체구조할당은 인벤토리에서 필요한 아이템만 꺼내
쓰는거라고 생각하면 편할듯

리액트에서 constext를 사용할때
다른 컴포넌트에서 context를 쓸 때
{아이템1, 아이템2} = constext(템창)

이렇게 꺼내왔던 것처럼 

*************************************************/

// 6-1. 객체 생성시 키 생략하기
// 리터럴 단축속성문법 (ES6 부터 도입) // 작성형식: person2 참고
// 객체를 생성할 떄 프로퍼티 키를 변수 이름을 생략 가능

const name2 = "박챠챠";
const home = "우리집";
const person2 = {name2, home};
const person3 = {name2:"시부레", home:"보내줘"};

console.log("person2",person2);
// 결과: person2 { name2: '박챠챠', home: '우리집' }
console.log("person3",person3);
// 결과: person3 { name2: '시부레', home: '보내줘' }


//7. 비구조화 할당 사용하기 = 객체 구조 분해 할당
// 비구조화 할당이란? 객체나 배열에서 값을 추출하여 변수에 할당하는 간결하고 편리한 방법
// 이것도 그냥 쉽게 인벤토리에서 템 꺼내다 쓰는거라 이해하면 편할듯

const makeItem = ({name, color, effect}) =>{
    return{
        name,
        color
    }
}

//  그 리액트에서 cdn 방식으로 사용할때 배웠던 기능!!! 기억난다 기억난다
const character = makeItem({name:"고기고기", color:"red"});
console.log(character);
// 결과: { name: '고기고기', color: 'red' }

// 8. 동적 속성 이름
// ES6에서 추가된 긴으! 객체의 키를 동적으로 설정 가으

const nameKey = "name";
const emailKey = "email";
const person4 = {
    [nameKey] : "김철수찰스철수",
    [emailKey] : "aaaa@aaaa.com"
};

console.log(person4);
//결과: { name: '김철수찰스철수', email: 'aaaa@aaaa.com' }


// 9. !! 연산자를 이용하여 Boolean 값으로 바꾸기
//  !! = 이중 논리 NOT 연산자
// @, null, 빈문자열, undefined, NaN를 false or ture로 변경할 수 있다

function check(variable) {
    if(!!variable){
        console.log(variable)
    }
    else{
        console.log("잘못된 값");
    }
}//check

check(null); //잘못된 값
check(3.14); //3.14
check(undefined); //잘못된 값
check(0); //잘못된 값
check("good"); //good
check(""); //잘못된 값
check(NaN); //잘못된 값
check(5); //5