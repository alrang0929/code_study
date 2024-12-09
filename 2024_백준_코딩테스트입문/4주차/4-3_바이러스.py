# https://www.acmicpc.net/problem/2606
def count_infected_computers(n, connections):
    # 그래프 초기화 (인접 리스트)
    graph = [[] for _ in range(n + 1)]
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)  # 무방향 그래프이므로 양방향 추가

    # DFS 탐색 함수
    def dfs(node):
        nonlocal infected_count
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                infected_count += 1
                dfs(neighbor)

    # DFS 초기화
    visited = [False] * (n + 1)
    infected_count = 0
    dfs(1)  # 1번 컴퓨터에서 시작

    return infected_count

# 입력 처리
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 수
connections = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(count_infected_computers(n, connections))
