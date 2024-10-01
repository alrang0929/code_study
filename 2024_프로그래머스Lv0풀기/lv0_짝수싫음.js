function solution(n) {
    var answer = [];
 for(let i = 0 ;  i <= n ; i++){
        if(i%2 !== 0){
           answer.push(i);
           }
 }
   
    return answer;
}

// 1. n의 짝홀 여부 확인 (/2를 한 후 나머지 x? 짝 o = 홀)
// 1-2. 짝이냐? n -1 하고 다시 올려
// for문으로 배열 돌려서 answer에 푸쉬