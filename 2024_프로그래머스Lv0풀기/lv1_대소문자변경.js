const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
//  결과값을 담기위한 배열
    let resultArr = [];
for(let i = 0; i < str.length ; i++){
    let target = str[i];
    if(target !== target.toUpperCase()){
      target = target.toUpperCase();
    }else{
       target = target.toLowerCase();
    }
    resultArr.push(target)
    
}    
    console.log(String(resultArr).replaceAll(",",""));
});

/* 
[문제풀이 방법]
1. for문으로 str 을 글자단위로 배열 생성하여 target에 담음
2. if 조건문으로 대소문자 구분 및 변환
3. 변환된 배열을 resultArr 배열에 담음
4. 후 콘솔에 문자값으로 변환하고 replaceAll로 콤마 제거하여 값 반환


>>> 나중에 replaceAll 말고 join도 함 써보기 


*/