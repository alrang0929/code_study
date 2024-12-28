# https://www.acmicpc.net/problem/14630
'''

[핵심 문장]
로봇의 현재 상태에서 부품의 형태가 가까운 변신일수록 돈이 적게 들고 먼 형태일수록 돈이 많이 드는 구조
부품의 형태는 숫자로 나타낼 수 있고, 로봇의 상태는 그 숫자들의 모임으로 나타낼 수 있다

변신에 필요한 돈은 각 부품들의 숫자 차이를 제곱한 것의 합

 예를 들어 로봇의 현재 상태가 123이고 다른 상태가 222라고 한다면 변신에 필요한 돈은 (1-2)2 + (2-2)2 + (3-2)2인 2
 
 돈을 가장 적게 사용해서 승균이가 원하는 변신 상태
 
'''

import heapq

def calculate_cost(part1, part2):
    """
    두 블록 간의 비용을 미리 계산
    """
    return sum((part1[i] - part2[i]) ** 2 for i in range(len(part1)))

def dijkstra(start, end):
    """
    다익스트라 알고리즘을 사용해 최소 비용 계산
    """
    distance[start] = 0
    heap = [(0, start)]  # 시작 노드
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        # 이미 처리된 경우 스킵
        if distance[current_node] < current_dist:
            continue
        
        # 현재 노드와 연결된 모든 노드 탐색
        for next_node, cost in graph[current_node]:
            new_cost = current_dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

# 입력 처리
n = int(input())
parts = [[]] + [[int(x) for x in input()] for _ in range(n)]
start, end = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        cost = calculate_cost(parts[i], parts[j])
        graph[i].append((j, cost))
        graph[j].append((i, cost))

# 최단 거리 배열 초기화
INF = float('inf')
distance = [INF] * (n + 1)

# 다익스트라 실행
dijkstra(start, end)

# 결과 출력
print(distance[end])
