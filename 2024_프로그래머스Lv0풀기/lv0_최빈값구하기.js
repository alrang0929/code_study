function solution(array) {
  
    const sortArray = array.sort((a,b)=> a-b);
    let cnt = 0;
    let moderCnt = -1;//최빈값
    let moderRepeatCnt = 0;//최빈값이 될때 몇번 반복했는지
    let isDubModer =false ; //중복 최빈값
    let reCnt = 0; // 현재 똑같은 숫자가 몇번 등장했는지
    let beforNum = -1; //현재의 이전 숫자
    

    while(cnt < array.length){
        if(beforNum !== sortArray[cnt]){
            reCnt= 1;
        }else{
            //동일한 값일 경우
            reCnt++;
        }//else
        if(reCnt === moderRepeatCnt && moderCnt !== array[cnt]){
            isDubModer = true;
        }
        if(reCnt >moderRepeatCnt){
            // 최빈값이 바뀌는 순간
            moderCnt = array[cnt];
            moderRepeatCnt = reCnt;
            isDubModer = false;
        }//if
         beforNum = array[cnt];
        cnt++;
    }//while
    if(isDubModer){return -1}
    else{
          return moderCnt;
    }
}



// 1. 앞에서 부터 숫자를 확인하며 수량 확인
// 2. 최빈값을 그때그때 기록