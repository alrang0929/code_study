# https://www.acmicpc.net/problem/1697

import sys
from collections import deque

input = sys.stdin.readline
# n = 수빈 위치 => 현재 위치, k = 동생 위치
n, k = tuple(map(int,input().split()))
# 이동이 가능한 경우

def dfs(n, k):
    # 유효범위 내 위치제한
    visited = [False] * 100001

    queue = deque([(n, 0)])
    visited[n] = True
    
    while queue: 
        current, time = queue.popleft()

        # 동생의 위치일 때 = time 반환
        if current == k:
            return time

        # 이동 가능한 위치 탐색
        for next_move in (current - 1), (current + 1), (current * 2):
            if 0 <= next_move <= 100000 and not visited[next_move]:
                visited[next_move] = True
                # 현재위치 전달, 1초 증가
                queue.append((next_move, time+1))
print(dfs(n,k))