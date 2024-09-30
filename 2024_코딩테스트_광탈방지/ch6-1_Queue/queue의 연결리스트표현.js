// Queue의 연결리스트 표현

class Node{
    // Node 생성 클래스 설정
    constructor(value){
        this.value = value;
        this.next = null;
    } //constructor
}//Node

class Queue {
    /************************************* 
    
    Queue의 기본구성
    1.enqueue
    2. dequeue
    3. peek
    
    *************************************/
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }//constructor

    enqueue(newValue){
        const newNode = new Node(newValue);
        if(this.head === null){
            this.head = this.tail = newNode; 
        }//if
        else{
            this.tail.next = newNode;
            this.tail = newNode;
        }//else

        this.size += 1;
    }//enqueue

    dequeue(){

        if(this.head === null){
            return null // or 에러처리
        }//if
        const value = this.head.value;
        this.head = this.head.next;
        this.size -= 1;

        if(this.head === null){
            this.tail = null; // queue가 비어있을 경우 tail도 null 처리
        }//if

        return value;
    }//dequeue

    peek(){
        if(this.head === null){
            return null // or 에러처리
        }//if
        return this.head.value;
    }//peek
}//Queue


// 대상선정
const queue = new Queue();
queue.dequeue(1);
queue.dequeue(2);
queue.dequeue(4);

console.log(queue.dequeue());

queue.dequeue(8);

console.log(queue.peek());
console.log(queue.dequeue());
console.log(queue.dequeue());