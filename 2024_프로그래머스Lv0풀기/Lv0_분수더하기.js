
/* 

문제:

첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 <numer1, denom1, numer2, denom2 < 1,000
입출력 예
numer1	denom1	numer2	denom2	result
1	2	3	4	[5, 4]
9	2	1	3	[29, 6]

*/


function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    const denom = denom1 * denom2;
    const numer = numer1 * denom2 + numer2 * denom1;
    
let gcd = 1; //최대공약수 변수
let i = 2; //나눠지는지 체크..

//smaller는 비교대상일뿐!!! 햇갈리지!! 말자!!!!!!!
const smaller = Math.min(denom,numer) //Math 변수로 작은 수 퉤
// i가 smaller보다 작거나 같을 때 까지 반복해
while(i <= smaller){
    // 화살표 순서 바뀌면 계산 안되더라..억울
    
    // i로 numer와 denom을 나눌 수 있다면? i = 최대공약수
    //따라서 최대공약수 변수인 gcd 를 i로 갱신
    if(numer % i === 0 && denom % i ===0){
        gcd = i;
    }//if
    // 그것이 아닐 경우 i를 1씩 증가 시키며 최대공약수 탐색
    i++
}
    return [numer/gcd,denom/gcd]

//     1. 분모 덧샘
//     2. 분자분모의 최대 공약수로 나눔
//      2-1. 분자 분모중 작은 수 찾음
//      2-2. 작은수를 분자분모로 나눠보기
//     2-2-1. 둘다 나누어 떨어지면 그 나눈 수가 최대 공약수
//     2-2-2. 안 나눠지면 작은수에 -1을 하며 2 반복
    
}