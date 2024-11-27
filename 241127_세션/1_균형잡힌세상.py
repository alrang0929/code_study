'''
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
[입력]
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
[입력예제]
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
[예제출력]
yes
yes
no
no
no
yes
yes
1. 문제 분석
1.문자열에서 **소괄호 ()**와 **대괄호 []**의 균형을 확인합니다.
2. 문자열이 "균형잡힌 문자열"인지 판단하려면:
    열린 괄호는 스택에 추가합니다.
    닫힌 괄호는 스택의 맨 위와 짝이 맞는지 확인 후 제거합니다.
    모든 문자를 처리한 후:
        스택이 비어 있으면 균형이 맞음.
        스택에 값이 남아 있으면 균형이 맞지 않음.
3. 문자열의 나머지 문자(영문자, 공백 등)는 무시합니다.
4. 입력 종료 조건으로 맨 마지막에 점(.)만 들어오는 경우가 있습니다. 이를 "처리해야" 합니다.
'''
# import sys
# 입력
# 무한루프
# 무한루프 안에 입력을 받는 형식으로
import sys
sys.stdin = open("input.txt","r")

while(True):
    line = input()
    # stack 선언
    stack = []
    # break (.) 종료
    if line == ".":
        break
    for char in line:
        # 열린 괄호 "(" or "["는 스택에 추가
        if char == "("or char == "[" :
            stack.append(char)
        # 닫힌 괄호 ") ]"는 짝이 맞는지 확인 후 제거
        elif char == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                # 비어있지 않으면 stack )을 추가
                stack.append(char)
        elif char == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                # 비어있지 않으면
                stack.append(char)
    # 스택이 비어있지 않으면
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
        
        
        # 시작시간: 7:50 / 끝난시간: 9:00