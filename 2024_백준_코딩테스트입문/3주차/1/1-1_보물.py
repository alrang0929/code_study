# https://teamsparta.notion.site/1-14a2dc3ef51481e481a1c5429fd33125

import sys,heapq

input = sys.stdin.read
data = input().strip().split("\n")

N = int(data[0])
A = list(map(int, data[1].split()))
B = list(map(int, data[2].split()))
S = 0


heapq.heapify(A)

max_heap = [-v for v in B]
heapq.heapify(max_heap)

for _ in range(N):    
    
    min_A = heapq.heappop(A)
    max_B = -heapq.heappop(max_heap)
    S += min_A * max_B
    
print(S)