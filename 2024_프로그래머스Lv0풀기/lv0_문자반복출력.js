/************************************************* 
[문제]
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에
들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록
solution 함수를 완성해보세요.
*************************************************/



function solution(){
    const my_string = "hello";
    const n = 3;
    let answer = "";
    let repeatStr = [];
    for(let i = 0; i < my_string.length ; i++){
       repeatStr.push(my_string[i].repeat(n));
   }
   return answer = String([...repeatStr]).replaceAll(",","");
}

solution();


/* 

[문제 해결 순서]

1. 문자열을 1개 단위로 쪼개서 반복 처리

- for문을 돌려 처리함
1) 문자열 길이만큼 증가시키며 반복
2) 그 결과값을 repeatStr 배열에 담음
3) 배열 합침 + 문자값으로 변환
4) 결과값이 "hhh,eee" 이런식으로 나옴
따라서 replaceAll을 사용하여 콤마 삭제
*/