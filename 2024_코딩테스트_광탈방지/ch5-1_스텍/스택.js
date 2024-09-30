// 스택 메모리 예시

//1. sum함수 실행
function sum(a, b) {
  return a + b;
}
// 실행 끝! pop으로 소멸

// 2. 아까 반환된 값으로 실행 즉, value = a+b
function print(value) {
  console.log(value);
}
print(sum(5, 10));

// stack을 js로 구현한다면?
// [1. Array로 구현]
const stack = [];

stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack);

// pop
stack.pop();
console.log(stack);

// get top
console.log(stack[stack.length - 1]);

// Linked List로 구현////////////////////////////////////////

// 구성요소 /////////////////////////////////////////////////////
// 요소Node
class Node {
  // constructor: 생산자
  constructor(value) {
    // 값과 포인터로 구성
    // 노드가 생성될 때는 포인터가 아무것도 가리키지 않음!
    this.value = value;
    this.next = null;
  }
} //node

// 단일연결리스트
class Stack {
  // node끼리 엮어주는 역할 생성자
  constructor() {
    this.top = null;
    this.size = 0;
  } // constructor

  push(value) {
    //1. currentNode 변수 생선, top 요소를 담음
    // 값을 찾기 전까지 while 메서드을 통해 순회 순회할 예정
    const node = new Node(value);
    node.next = this.top;
    this.top = node;
    this.size += 1;
  } //push

  pop() {
    const value = this.top.value;
    this.top = this.top.next;
    this.size -= 1;
    return value;
  } //pop

  size() {
    return this.size;
  } //size
} //Stack


const stack2 = new Stack();
stack2.push(1);
stack2.push(2);
stack2.push(3);

console.log(stack.pop()); //3

stack2.push(4);
console.log(stack.pop()); //4
console.log(stack.pop()); //2

[ 1, 2, 3 ]
[ 1, 2 ]
2
2
1
undefined
