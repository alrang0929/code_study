function solution(numbers) {

    //     1. 누적함수
        let sum = 0;
        let cnt =0;
        
        while(cnt < numbers.length){
            sum = sum + numbers[cnt];
            cnt++;
        }
        return sum/numbers.length;
    }

    // for of문 사용예시
    function solution(numbers) {

        //     1. 누적함수
            let sum = 0;
            for(const a of numbers){
                sum += a
            }
            return sum/numbers.length;
        }