'''

이번 계절학기에 심리학 개론을 수강 중인 평석이는 오늘 자정까지 보고서를 제출해야 한다. 
보고서 작성이 너무 지루했던 평석이는 노트북에 엎드려서 꾸벅꾸벅 졸다가 제출 마감 1시간 전에 깨고 말았다. 
안타깝게도 자는 동안 키보드가 잘못 눌려서 보고서의 모든 글자가 A와 B로 바뀌어 버렸다! 
그래서 평석이는 보고서 작성을 때려치우고 보고서에서 '좋은 단어'나 세보기로 마음 먹었다.

평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 
그 단어는 '좋은 단어'이다. 평석이가 '좋은 단어' 개수를 세는 것을 도와주자.

첫째 줄에 단어의 수 N이 주어진다. (1 ≤ N ≤ 100)

3
ABAB
AABB
ABBA

[출력값]
2

'''

import sys
sys.stdin = open('input.txt','r')

# 입력 처리
n = int(input())  # 단어의 개수
words = [input().strip() for _ in range(n)]  # 단어 리스트

# 좋은 단어 개수
good_word_count = 0

# 각 단어를 검사
for word in words:
    # LIFO구조를 가져 짝을 찾는데 적합함
    # 왜? 이전 요소를 기억하고 현재 요소와 비교할 수 있음
    stack = []
    for char in word:
        if stack and stack[-1] == char:  # 스택의 맨 위 글자와 같으면 제거
            stack.pop()
        else:  # 그렇지 않으면 추가
            stack.append(char)
    
    # 스택이 비어 있으면 좋은 단어
    if not stack:
        good_word_count += 1

# 결과 출력
print(good_word_count)