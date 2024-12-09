# https://www.acmicpc.net/problem/24444

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = order[0]
    order[0] += 1
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == 0:  # 방문하지 않은 정점만 탐색
                visited[neighbor] = order[0]
                order[0] += 1
                queue.append(neighbor)

# 입력
N, M, R = map(int, input().split())  # 정점 수, 간선 수, 시작 정점
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 정렬 (인접 정점 오름차순 방문을 위해)
for key in graph:
    graph[key].sort()

# 방문 순서 기록 배열 및 BFS 수행
visited = [0] * (N + 1)  # 방문 순서 저장 (0 초기화)
order = [1]  # 순서를 기록할 변수 (리스트 형태로 사용)

bfs(R)

# 결과 출력
for i in range(1, N + 1):
    print(visited[i])
