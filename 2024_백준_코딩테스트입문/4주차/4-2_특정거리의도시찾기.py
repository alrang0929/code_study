#https://www.acmicpc.net/problem/18352

'''
- 최단거리 k인 도시를 찾아내는 것이 목표
- 인접 리스트를 사용해 그래프 표현

2. 최단 거리 계산은 BFS로
- 모든 간선의 거리가 1이므로 BFS를 통한 특정거리 K에 도달한 노드만 필터링

3. 예외 처리
- 만약 BFS 탐색 결과, K거리에 도착한 노드가 없다면 -1 출력

'''

import sys
from collections import deque
input = sys.stdin.read

def find_city(n, k, x, roads):
    # 그래프 초기화 (인접 리스트)
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
    
    # BFS 초기화
    queue = deque([x])
    visited = [-1] * (n + 1)  # 방문 및 거리 배열
    visited[x] = 0
    result = []

    while queue:
        current = queue.popleft()
        
        # 현재 도시의 거리가 K면 결과 저장
        if visited[current] == k:
            result.append(current)
            continue
        
        # 이웃 노드 탐색
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 미방문 노드
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    return sorted(result) if result else [-1]

# 입력 처리
data = input().split()
n, m, k, x = map(int, data[:4])
roads = [tuple(map(int, data[i:i+2])) for i in range(4, len(data), 2)]
result = find_city(n, k, x, roads)
sys.stdout.write('\n'.join(map(str, result)) + '\n')
