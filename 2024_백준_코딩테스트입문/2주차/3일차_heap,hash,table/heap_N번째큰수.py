# https://www.acmicpc.net/problem/2075
'''
첫번째 줄에 N번째 큰 수를 출력한다

5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49

[결과]
35

'''
'''

import heapq

# 최소 힙
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 3)
print(heapq.heappop(min_heap))  # 1

# 최대 힙
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))  # 5

'''

# import sys
# import heapq 
# sys.stdin = open("input.txt","r")

# 1. 입력받기
# n = int(input())
# cnt = n*n
# numbers =[]

# 2. 숫자 입력받기
# for _ in range(n):  
    # n줄에 걸쳐 숫자가 주어진다고 가정
    # numbers.extend(map(int, input().split()))  
    # 한 줄씩 읽어 숫자 리스트에 추가
'''
extend(): 리스트를 확장하여 새로운 요소를 개별적으로 추가
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # 리스트 확장
print(my_list)  # [1, 2, 3, 4, 5, 6]

append(): 리스트에 하나의 원소 추가
my_list = [1, 2, 3]
my_list.append([4, 5, 6]) # 리스트 자체를 하나의 요소로 추가
print(my_list)  # [1, 2, 3, [4, 5, 6]]

'''

# min_heap =[]

# for num in numbers:
#     if len(min_heap) < n:  # 힙 크기가 n보다 작을 경우
#         heapq.heappush(min_heap, num)
#     elif min_heap[0] < num:  # 현재 힙의 최소값보다 큰 경우 교체
#         heapq.heappop(min_heap)
#         heapq.heappush(min_heap, num)

# print(min_heap[0])  # N번째 큰 수 출력

# 메모리 초과..

import sys
import heapq

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])  # 행렬 크기
min_heap = []
cnt = n * n
# 숫자 처리
for _ in range(cnt):  # 각 행의 숫자 처리
    num = int(data[1:])  # 한 줄씩 숫자 읽기
   
    if len(min_heap) < n:  # 힙 크기가 n보다 작으면 추가
        heapq.heappush(min_heap, num)
    elif min_heap[0] < num:  # 힙의 최솟값보다 큰 경우 교체
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, num)

# 힙의 최솟값이 n번째 큰 값
print(min_heap[0])

'''

import heapq

n = int(input())
min_heap = []
cnt = n * n

for _ in range(cnt):
    num = int(input())
    if len(min_heap) < n:
        heapq.heappush(min_heap, num)
    elif min_heap[0] < num:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, num)

print(min_heap[0])

'''
