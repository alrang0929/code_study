'''
https://www.acmicpc.net/problem/16466

[조건]
1.1차, 2차 티켓팅이 있음
2. N = 1차 티켓팅에서 팔린 티켓 수를 알고 있음.
3. 2차 티켓팅에서 가질 수 있는 가장 작은 수를 알아낼 것

첫째줄 = N
둘째줄 = An...

예시를 참고해볼 때

5<== N
4 1 2 7 8 <===A

[결과]
3

1부터 탐색하여 제일 작은 수를 찾는 것
따라서 아래처럼 하면 되지않을까..?

1. 1~n 까지 배열을 생성
2. set을 통한 중복값 제거, 집합 만들기
3. min 사용


'''

import sys
input = sys.stdin.read
# splitlines 포기..
data = input().strip().split("\n") 
N = int(data[0])# 1차 때 팔린 티켓수
second_ticket = set(map(int, data[1].split()))# 남은 2차 티켓
ticket = 1 #최소 티켓
answers = []

# while문을 돌면서 찾기
while True:
    if ticket in second_ticket:
         answers.append(ticket)
    else:
        break
    ticket += 1
    
print(len(answers)+1)