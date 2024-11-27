# import sys
# sys.stdin = open('input.txt','r')
# from collections import deque

'''

정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.

push_back X: 정수 X를 덱의 뒤에 넣는다.

pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

[예제]
15 // 명령의 수

push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front


[출력]
2
1
2
0
2
1
-1
0
1
-1
0
3

'''
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.read
data = input().splitlines() #문자열을 리스트형으로 변경

'''
['22', 'front', 'back', 'pop_front', 'pop_back', 'push_front 1', 'front', 'pop_back', 'push_back 2', 'back', 'pop_front', 'push_front 10', 'push_front 333', 'front', 'back', 'pop_back', 'pop_back', 'push_back 20', 'push_back 1234', 'front', 'back', 'pop_back', 'pop_back']

'''

cnt = int(data[0])  # 명령 수
commands = data[1:]  # 명령 리스트
decue = deque() 

for command in commands:
    if command.startswith("push_back"):
        _, num = command.split()
        decue.append(int(num))

    elif command.startswith("push_front"):
        _, num = command.split()
        decue.appendleft(int(num))

    elif command == "front":
        print(decue[0] if decue else -1)

    elif command == "back":
        print(decue[-1] if decue else -1)

    elif command == "size":
        print(len(decue))

    elif command == "empty":
        print(1 if not decue else 0)

    elif command == "pop_front":
        print(decue.popleft() if decue else -1)

    elif command == "pop_back":
        print(decue.pop() if decue else -1)
