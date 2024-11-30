import heapq
# import sys

# 입력 처리
# sys.stdin = open("input.txt", "r")  # 파일에서 입력 받기
n = int(input())  # 후보의 수
dasom = int(input())  # 다솜의 표
votes = []  # 다른 후보들의 표

# 나머지 후보들의 표 입력
for _ in range(n - 1):
    votes.append(int(input())) 

count = 0  # 매수 횟수 초기화

# 1-2. votes를 최대 힙으로 관리하기 위한 음수로 저장
max_heap = [-v for v in votes]  # 음수로 변환하여 최대 힙 구성
heapq.heapify(max_heap)  # 리스트를 힙 구조로 변환 
# O(n)

# 2. 예외 처리: 후보가 다솜 혼자인 경우
if n == 1:
    print(0)  # 매수 필요 없음
else:
    # 2-1. 다솜의 표가 최대가 될 때까지 반복
    while max_heap and -max_heap[0] >= dasom: #O(n log n) : 최대 횟수가 정해져있음
        # 가장 많은 표를 가진 후보를 매수
        max_votes = -heapq.heappop(max_heap) #O(log n)
        dasom += 1
        count += 1
        max_votes -= 1

        # 매수 후 표가 남아 있으면 다시 힙에 삽입
        if max_votes > 0:
            heapq.heappush(max_heap, -max_votes)#O(log n)
            
    print(count)
    
# 전체 시간복잡도: O(n log n)