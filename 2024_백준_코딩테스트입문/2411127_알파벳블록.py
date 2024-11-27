import sys
sys.stdin = open('input.txt','r')
from collections import deque
'''
스타는 알파벳 블록을 일렬로 조립하여 문자열을 만드는 게임을 만들었다. 각 블록에는 문자 하나가 적혀 있으며 게임에는 각각 다음 기능을 수행하는 세 개의 버튼이 있다.

- 문자열 맨 뒤에 블록 추가
- 문자열 맨 앞에 블록 추가

- 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거

게임은 처음에 빈 문자열로 시작하며 빈 문자열일 때 문자열을 구성하는 블록 중 가장 나중에 추가된 블록을 제거하는
버튼을 누를 경우 아무런 동작도 하지 않는다. 버튼을 누른 횟수와 누른 버튼이 순서대로 주어질 때 완성된 문자열을 구하여라.


1 c : 문자열 맨 뒤에 c가 적힌 블록 추가
2 c : 문자열 맨 앞에 c가 적힌 블록 추가
3 : 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거

[예제]
5
1 a
2 b
2 c
3
3

[예제 출력]

a


#### 언패킹 문법
data = (100, 200, 300)
_, b, _ = data  # b = 200
print(b)  # 출력: 200

'''

# 1. 문자열이 들어온 순서를 기억해야됨
# 2. deque를 활용한 리스트 조종
input = sys.stdin.read
data = input().splitlines() #여러줄 입력처리
num = int(data[0]) #버튼을 누른 횟수 5
# strip() : 문자열 공백 제거!
item = data[1:] 
strArr = deque() #문자열 블록 정리
history = [] #문자열 순서 기록
# history의 번호표를 기준으로 순차적으로 3(가장 나중에 추가된 블록 제거)실행, 따라서 append 로 순차적으로 메모

for item in item:
    #1. startswith(시작하는문자, 시작지점)!! 즉 1로 시작하는 문자열이냐?
    if item.startswith("1"):
         _, char = item.split() #문자열 맨뒤에 추가
         strArr.append(char) 
         history.append(("1",char)) #순번과 함께 기록 
    elif item.startswith("2"):
         _, char = item.split() #문자열 맨앞에 추가
         strArr.appendleft(char)
         history.append(("2",char)) #순번과 함께 기록 
    elif item.startswith("3"):
         if history: #기록이 있을 때 실행
             last_action, last_char = history.pop() #가장 나중에 들어온 문자열 제거 후, 제거한 문자열에서 첫번째 문자열과 마지막 문자열 가져옴
             if last_action == '1':
                 strArr.pop()
             elif last_action == '2':
                strArr.popleft()
                
print("".join(strArr))



