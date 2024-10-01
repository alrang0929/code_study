function solution(array) {
    // 원본값 보존을 위해 [...] 스프레드 연산자로 값 복사하여 원본 보존
    const sortArray = [...array].sort((a,b)=> a-b); // 배열 복사후 정렬
    var answer = sortArray[Math.floor(array.length/2)];
    
    return answer;
}