function solution(n) {
    const pizza = 6;
    let pizzaCnt = 1;
    
    while(true){
    if((pizza*pizzaCnt) % n === 0){
       return pizzaCnt;
   }
      pizzaCnt++;

    }//while
  
}

/* 
핏쟈..
나머지 수만 안나오면 되니까 ..
배수가 나올 떄까지 곱하면되지요..

*/