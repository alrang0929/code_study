//시작 시간을 구함
console.log("start!");
const start = new Date().getTime();

// 2. 로직 작동
const N = 1000000000;
let total = 0;

for (let i = 0; i < N; i += 1) {
  total += i;
} //for

// 3. 끝나는 시간
const end = new Date().getTime();

//  끝 - 시작 = 로직 작동 시간
console.log(end - start);
console.log("finish!");


/* 
1. 날짜 + 시간을 가져오는 메서드로 start 선언

2. const N < 상수로 테스트를 위한 값 설정
3. for문으로 코드 성능 테스트 시작
    for문 해석:
    
    조건: i는 0 이다, i를 돌려라 N(10억)보다 커질떄까지 
    이때 i 는 1이다

    total 은 i와 같다 << 즉 10번 돌겠지..

end에 코드 끝나는 시간 담기고 측정값을 console로 퉤

*/