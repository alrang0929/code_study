function solution(n) {
    var answer = 0;
    
    if(n<=7){
        answer = 1;        
    }else{
        answer = Math.ceil(n/7);
    }
    return answer;
}

// 7이하 : 1판
// 그 이상? n/7 해서 올림하면 다 먹을 수 있음
// 올림 메서드 Math.ceil 사용