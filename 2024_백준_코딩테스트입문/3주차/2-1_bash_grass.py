# https://www.acmicpc.net/problem/6186

'''
그래프 탐색을 통해 해결할 것
풀 덩어리 연결된 구성 요소를 보고 규칙 찾기
풀 덩어리 = #, 인접한 #이 하나의 덩어리를 형성

연결 요소의 개수를 세는 문제

문제 해결 과정:
1. 그래프 탐색을 통한 덩어리 찾기.
    연결된 #들을 하나의 덩어리로 보고 이 덩어리를 한 번씩만 탐색
2. BFS나 DFS를 사용하여 각 덩어리의 크기를 찾아내고 방문 지점은 다시 방문하지 않도록 처리


알고리즘:
1. 입력 처리:
주어진 지도에 대한 R,C 값을 입력받음
그에 따른 목초지의 상태를 리스트 전달받기

2. DFS(깊이 우선 탐색)
한 셀을 시작으로 DFS를 수행하여 연결된 모든 #을 찾아 방문 처리

3. 탐색 수행: 지도에서 아직 방문하지 않은 #이 발견되면 그 셀을 시작으로 DFS 수행, 덩어리 1 증가
결과 출력: 덩어리 개수 출력 

'''

# 2. DFS(깊이 우선 탐색)
def dfs(grid, visited, r, c, R, C):
    # 상, 하, 좌, 우로 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(r, c)]  # DFS를 위한 스택
    visited[r][c] = True  # 방문 처리

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))
                
                
def count_grass_clusters(R, C, grid):
    visited = [[False] * C for _ in range(R)]  # 방문 여부를 확인할 배열
    cluster_count = 0
  # 모든 셀을 탐색
    for i in range(R):
        for j in range(C):
            #아직 방문하지 않은 '#'이 있을 경우
            if grid[i][j] == '#' and not visited[i][j]:
                # 새로운 덩어리 발견
                #  DFS를 호출하여 연결된 모든 '#를 방문'
                dfs(grid, visited, i, j, R, C)
                cluster_count += 1  # 덩어리 수 증가
    # 덩어리의 수를 반환
    return cluster_count

# 1. 입력 처리 
R, C = map(int,input().split())#R=행, C = 열
# 2차원 리스트로 저장
grid = [input().strip() for _ in range(R)]

# 풀이 실행
result = count_grass_clusters(R, C, grid)
print(result)