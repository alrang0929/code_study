# https://www.acmicpc.net/problem/2644
'''

두 사람 간의 촌수를 계산 = 두 노드 사이의 거리 찾기

사람들 = 노드
부모-자식관계 = 간선
촌수를 계산해야 하는 서로 다른 두 사람의 번호 = 시작점과 끝점을 정하고 최단 경로를 찾아야 됨


입력방식:
n = 전체 사람의 수 


'''

def calculate_kinship():
    # 입력값 받는 부분
    n = int(input())
    start, end = map(int, input().split())
    m = int(input())
    relations = []
    for _ in range(m):
        x, y = map(int, input().split())
        relations.append((x, y))

    # 그래프를 인접 리스트로 표현합니다.
    graph = [[] for _ in range(n + 1)]
    for x, y in relations:
        graph[x].append(y)
        graph[y].append(x)

    # DFS를 사용하여 촌수를 찾습니다.
    visited = [False] * (n + 1)
    result = []

    def dfs(v, num):
        visited[v] = True
        num += 1

        if v == end:
            result.append(num)
            return

        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, num)

    dfs(start, 0)
    if len(result) == 0:
        print(-1)
    else:
        print(result[0] - 1)

# 함수 호출
calculate_kinship()