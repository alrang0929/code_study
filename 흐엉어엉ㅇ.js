const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on('line', function (line) {
  input.push(line); 
  rl.close(); // 입력 스트림 종료
}).on('close', function () {
  const n = Number(input[0]);
  for (let line = 1; line <= n; line++) {
    let starStr = "";
    for (let cnt = 0; cnt < line; cnt++) {
      starStr = starStr + "*";
    }
    console.log(starStr);
  }
});



const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
   const n = Number(input[0]);
        for (let line = 1; line <= n; line++) {
        let starStr = "";
        for (let cnt = 0; cnt < line; cnt++) {
            starStr = starStr + "*";
        }
        console.log(starStr);

    }//for

};

