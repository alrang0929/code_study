'''
https://www.acmicpc.net/problem/26042


5 <== 테스트 케이스
1 2 <== 각 학생들의 줄 수 
1 1
2
1 3
2

[유형 / 번호]
1유형 = 맨 뒤에 추가
2유형 = 맨 뒤 제거
'''

import sys
from collections import deque

load = sys.stdin.read
data = load().strip().split("\n")

T = int(data[0])
waiting_list = data[1:]
max_size = 0  # 대기열의 최대 크기
min_last_student = None

# 변수 초기화
queue = deque()


for waiting in waiting_list:
    waiting_line = waiting.split()
    
    # 유형별 명령어 처리
    # 1유형: 큐에 학생 번호 추가
    if waiting_line[0] == "1":
        student_num = int(waiting_line[1])
        queue.append(student_num)

        # 대기열 크기, 맨 뒤 학생 번호 갱신
        waiting_size = len(queue)
        if waiting_size > max_size:
            max_size = waiting_size
            min_last_student = queue[-1]
        elif waiting_size == max_size:
            min_last_student = min(min_last_student, queue[-1])

     # 2유형: 맨 뒤 번호 제거
    elif waiting_line[0] == "2":
        if queue:
            queue.popleft()
    
print(max_size)
print(min_last_student)