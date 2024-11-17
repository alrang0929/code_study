
/************ promise 사용방법 ******************************************/

// const myPromise = new Promise(function (resolve, reject) {
    //     if (false) {
        //       resolve(`Success`);
        //     } else {
            //       reject(`Failed`);
            //       /* 
            //       [오류발생]
            //       UnhandledPromiseRejection: reject가 발생할 경우 적절한 처리를 같이 해줘야함..그것이 catch
            //       */
            //     }
            //   }); // Promise
            //   // then: 성공한 경우 / catch: 실패한 경우
            
            //   // 아래와 같이메소드 체이닝 하여 사용 
            //   myPromise
            //   .then((value)=>{console.log(value)}).
            //   catch((value)=>{console.log(value)});
            
            
            
/************ async / await 사용방법 ******************************************/
// async 함수: async 키워드를 함수 선언 앞에 붙여 정의, 항상 promise를 반환함

// ex 

// async function fatchData() {
//     return `data loaded successfully`;
// }

// /* 
// 이는 아래 코드와 동일하다
//         async function fatchData() {
//             return Promise.reslove(`data loaded successfully`);
//         }
// */
// // fatchData의 결과
// fatchData(true).then(console.log);
// // fatchData() = Promise 객체

/*********************** 
await: 
기다리는 녀석, 프로미스의 완료를 기다리는 동안 ★함수의 실행을 일시적으로 중단! ★
promis가 끝난 후 함수 실행 재개
따라서 비동기 코드의 동기적 표현이 가능해짐, 코드 가독성도 항상됨
***********************/

async function fetchData() {
    try {
        // 1. data를 다 받은 후에
        const data = await fetch('https://jsonplaceholder.typicode.com/posts');
        // 2. 해당 코드를 출력해라
      const json = await data.json();
    //  await가 없을경우? Promise { <pending> } 이 출력됨. :
    // 왜? json이 실행이 완료되기 전에 코드 실행되자마자 console 이 실행됐기 때문에
      console.log(json);
    } catch (error) {
        // 코드 실행X, error가 발생했다면 해당 문구와 에러를 띄와라
      console.error("Data loading failed", error);
    }
  }
  
  fetchData();

  