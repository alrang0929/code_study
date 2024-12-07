# https://www.acmicpc.net/problem/24479
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global order
    visited[node] = order
    order += 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:  # 방문하지 않은 경우만 탐색
            dfs(neighbor)

# 입력 받기
N, M, R = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 정렬 (오름차순)
for key in graph:
    graph[key].sort()

# 방문 순서 기록
visited = [0] * (N + 1)
order = 1

# DFS 수행
dfs(R)

# 결과 출력
for i in range(1, N + 1):
    print(visited[i])