// 단일연결리스트 구현 코드

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
class SinglyLinkedList {
  // node끼리 엮어주는 역할 생성자
  constructor() {
    this.head = null;
    this.tail = null;
  } // constructor

  find(value) {
    //1. currentNode 변수 생선, head 요소를 담음
    // 값을 찾기 전까지 while 메서드을 통해 순회 순회할 예정
    let currNode = this.head;
    /************************************************** 
    
    while(): 컴퓨터에게 뭔가를 계속 시키는 주문!!
    while()의 조건문은 ture/false로 값을 반환함
     조건이 맞다면 코드 구역의 코드를 계속 반복함
    조건은 코드가 실행될 때 마다 감시
    조건에 따라 무한루프에 빠질 수 있으니 조심
    while()안의 코드는 들여쓰기를 해야 구분 가능
    
    **************************************************/
    while (currNode.value !== value) {
      //2. currNode의 값이 전달받은 value와 값지 않냐?
      // 2-1. 그렇다면 현재 노드의 다음 타겟을 담아라
      currNode = currNode.next;
    }
    //3. 값을 찾았다면 while 코드를 빠져나와 값을 currNode 에 반환!
    return currNode;
  } //find
  ////////////////////////////////////////////////////////////

  //맨앞에 추가해줘! append 추가 로직
  append(newValue) {
    //1. newValue의 값을 받아 Node 인스턴스를 생성하여 newNode에 담는다!
    const newNode = new Node(newValue);
    // 2. 만약 이 head의 값이 비어있냐?
    if (this.head === null) {
      //2-1 그렇다면 생성된 노드를 담아라!
      this.head = newNode;
      this.tail = newNode;
    } //if
    else {
      //3. 값이 존재하냐?
      //3-1 새로 생성된 값을 담아라!
      //마지막 노드의 다음 node에 newNode를 연결! 그러면 새로운 노드가 리스트의 일부가 된다
      this.tail.next = newNode;
      // tail은 항상 마지막 노드를 가리켜야 되기 때문에 newNode를 담는다!
      this.tail = newNode;
    } //else
  } //append

  /******************************************************************** 
  기존 리스트:  head -> node1 -> node2 -> tail (null)

newNode 추가 후: head -> node1 -> node2 -> newNode -> tail (null)
  
  ********************************************************************/

  //중간에 추가해줘! insert 로직
  insert(node, newValue) {
    /********************************************************** 
    결과를 미리 보자면...
    삽입 전:  ... -> node -> node.next -> ...
    삽입 후:  ... -> node -> newNode -> node.next -> ...
    **********************************************************/
    // 1. 파라미터로 전달받은 newValue로 newNode 인스턴스 생성
    const newNode = new Node(newValue);
    // 2. 새로운 노드의 next를 기존 노드의 next로 설정, 새로운 노드가 들어올 자리를 준비해줌
    newNode.next = node.next;
    // 3. 입력받은 노드를 새로 생성된 노드를 가리키게 함
    // : 기존 노드의 next를 새로운 노드로 설정!
    node.next = newNode;
  }

  // 삭제로직
  /* 
  삭제하려는 node의 이전 노드를 찾아
  이전 노드의 next를 삭제하려는 노드의 다음으로 연결


  예시해석:
  삭제 전 리스트: 1 -> 2 -> 3 -> 4 
  삭제할 값: 3
  
  1. prevNode는 1을 가리킴 
  2. prevNode.next.value (2)는 3과 다르므로, prevNode는 2를 가리키도록 이동
  3. prevNode.next.value (3)는 3과 같으므로 while문 종료
  4. prevNode.next는 3을 가리키고, null이 아니므로 if문 실행
  5. prevNode.next는 prevNode.next.next (4)를 가리키도록 변경
  6. 결과: 1 -> 2 -> 4 
  */
  remove(value) {
    // 1. prevNode 변수를 선언, 리스트 시작점(head)을 가리켜라
    let prevNode = this.head;
    // 2. 루프를 돌며 이전노트를 찾음!
    while (prevNode.next.value !== value) {
      // 2-1 prevNode의 다음 노드 값이 지금 value(=우리가 삭제하려는 것)와 다르냐?
      // 즉, 찾을 때 까지 루프를 돌라는 조건문

      //2-2 prevNode를 다음 노드로 이동시켜라. 한칸 앞으로!
      prevNode = prevNode.next;
    }
    // 그러면 prevNode에 삭제하려는 노드의 이전 노드가 담겨있음
    // 즉, prevNode.next는 삭제하려는 노드를 가리키고 있음!
    if (prevNode.next !== null) {
      // 삭제하려는 노드의 값이 null(=리스트의 끝)이 아니냐?
      // 그렇다면 삭제할 노드의 다음에 연결해라
      prevNode.next = prevNode.next.next;
    }
    // 4. 그러면 중간 노드는 아무것에도 연결되지 않았기 때문에 추후 가비지 컬렉션을 통해 메모리 상에서
    // 삭제됨
  } //remove

  display() {
    let currNode = this.head;
    let displayString = "!";
    while (currNode !== null) {
      displayString += `${currNode.value},`;
      currNode = currNode.next;
    } //while
    
    displayString = displayString.substr(0, displayString.length - 2);
    displayString += "]";
    console.log(displayString);
  } //display
} //SinglyLinkedList

const linkedList = new SinglyLinkedList();
linkedList.append(1);
linkedList.append(2);
linkedList.append(3);
linkedList.append(4);
linkedList.append(5);
linkedList.display();

console.log(linkedList.find(3));

linkedList.remove(3);

linkedList.display();
linkedList.insert(linkedList.find(2), 10);
linkedList.display();



/* 

최종정리


1. Node 클래스

연결 리스트의 기본 구성 요소인 노드를 나타냅니다.
각 노드는 value (저장되는 데이터)와 next (다음 노드를 가리키는 포인터)를 가집니다.
생성자(constructor)를 통해 새로운 노드를 생성할 때 value를 설정하고, next는 초기값으로 null을 갖습니다.


2. SinglyLinkedList 클래스

단일 연결 리스트를 나타냅니다.
head: 리스트의 첫 번째 노드를 가리키는 포인터
tail: 리스트의 마지막 노드를 가리키는 포인터
생성자(constructor)를 통해 새로운 연결 리스트를 생성할 때 head와 tail은 초기값으로 null을 갖습니다. (빈 리스트)


3. find(value) 메서드

연결 리스트에서 특정 값(value)을 가진 노드를 찾아 반환합니다.
currNode 변수를 사용하여 리스트의 head부터 시작하여 순차적으로 노드를 탐색합니다.
while 루프를 통해 currNode의 값이 찾으려는 value와 같아질 때까지 다음 노드로 이동합니다.
값을 찾으면 해당 노드(currNode)를 반환하고, 찾지 못하면 null을 반환합니다. (코드에는 명시적으로 null 반환이 없지만, while 루프를 끝까지 돌고 나면 currNode는 null이 됩니다.)


4. append(newValue) 메서드

연결 리스트의 맨 끝에 새로운 노드를 추가합니다.
새로운 노드(newNode)를 생성하고, newValue를 값으로 설정합니다.
리스트가 비어있는 경우(this.head === null), 새로운 노드를 head와 tail에 모두 할당합니다.
리스트가 비어있지 않은 경우, 현재 tail의 next에 새로운 노드를 연결하고, tail을 새로운 노드로 업데이트합니다.


5. insert(node, newValue) 메서드

연결 리스트의 특정 노드(node) 다음에 새로운 노드를 삽입합니다.
새로운 노드(newNode)를 생성하고, newValue를 값으로 설정합니다.
새로운 노드의 next를 기존 노드의 next로 설정합니다. (새로운 노드가 삽입될 위치를 준비)
기존 노드의 next를 새로운 노드로 설정합니다. (새로운 노드 삽입)


6. remove(value) 메서드

연결 리스트에서 특정 값(value)을 가진 노드를 삭제합니다.
prevNode 변수를 사용하여 삭제하려는 노드의 이전 노드를 추적합니다.
while 루프를 통해 prevNode 다음 노드의 값이 삭제하려는 value와 같아질 때까지 다음 노드로 이동합니다.
삭제하려는 노드를 찾으면(prevNode.next !== null), prevNode의 next를 삭제하려는 노드의 next.next로 연결하여 삭제합니다.
삭제하려는 값을 가진 노드를 찾지 못하면 아무 작업도 수행하지 않습니다.


7. display() 메서드

연결 리스트의 모든 노드의 값을 출력합니다.
currNode 변수를 사용하여 리스트의 head부터 시작하여 순차적으로 노드를 탐색합니다.
while 루프를 통해 currNode가 null이 아닐 때까지 각 노드의 값을 displayString에 추가합니다.
마지막 쉼표와 공백을 제거하고 대괄호를 추가하여 displayString을 완성합니다.
console.log를 사용하여 displayString을 출력합니다.


8. 실행 코드

SinglyLinkedList 클래스의 인스턴스(linkedList)를 생성합니다.
append 메서드를 사용하여 1부터 5까지의 값을 가진 노드를 차례로 추가합니다.
display 메서드를 호출하여 연결 리스트의 내용을 출력합니다.
find 메서드를 사용하여 값이 3인 노드를 찾고, 결과를 콘솔에 출력합니다.
remove 메서드를 사용하여 값이 3인 노드를 삭제합니다.
display 메서드를 호출하여 삭제 후 연결 리스트의 내용을 출력합니다.
find 메서드를 사용하여 값이 2인 노드를 찾고, 그 다음 위치에 insert 메서드를 사용하여 값이 10인 노드를 삽입합니다.
display 메서드를 호출하여 삽입 후 연결 리스트의 내용을 출력합니다.


*/