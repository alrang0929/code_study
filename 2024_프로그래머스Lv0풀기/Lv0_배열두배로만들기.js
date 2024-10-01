/* 
문제 설명
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
1 ≤ numbers의 길이 ≤ 1,000
입출력 예
numbers	result
[1, 2, 3, 4, 5]	[2, 4, 6, 8, 10]
[1, 2, 100, -99, 1, 2, 3]	[2, 4, 200, -198, 2, 4, 6]
입출력 예 설명
입출력 예 #1

[1, 2, 3, 4, 5]의 각 원소에 두배를 한 배열 [2, 4, 6, 8, 10]을 return합니다.
입출력 예 #2

[1, 2, 100, -99, 1, 2, 3]의 각 원소에 두배를 한 배열 [2, 4, 200, -198, 2, 4, 6]을 return합니다.

*/

function solution(numbers) {
     
    var answer = [];
    
    let i = 0;
    
    while(i < numbers.length){
        answer.push(numbers[i]*2);
        i++
    }
    
        
    return answer;
}

//1. numbers 안에 있는 요소들을 끄집어 내야됨
// 어떻게 꺼냄? Numbers = [1,2,3,4,5]
//여기서 1을 꺼낼려면? Numbers[0]

//값을 넣을 땐? push

//2. 요놈들을 꺼내 2배를 한 후 새 배열에 담아야

/* 
여기서 얻었던 팁..
코테는 일단 통과가 목표..!!

*/