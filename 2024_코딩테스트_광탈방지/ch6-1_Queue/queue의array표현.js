// Queue를 array로 표현한다면?

class Queue {
  // class 변수 생성
  constructor() {
    // 1. queue를 담는 배열
    this.queue = [];
    // 2. front index 요소
    this.front = 0;
    // 3. rear index 요소
    this.rear = 0;
  } //constructor;

  // stack의 pop part
  enqueue(value) {
    // rear = 뒷부분
    this.queue[this.rear++] = value;
  } //enqueue
  //   stack의 push part
  dequeue() {
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front += 1;
    return value;
  } //dequeue

//   queue의 가장 앞에 있는 배열을 알아내는 함수
  peek() {
    return this.queue[this.front];
  } //peek

//   queue의 크기
  size() {
    return this.rear - this.front;
  } //size
} //Queue

// 대상선정
const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(4);

console.log(queue.dequeue()); //1

queue.enqueue(8);

console.log(queue.size()); //3
console.log(queue.peek()); //2
console.log(queue.dequeue()); //2
console.log(queue.dequeue()); //4
