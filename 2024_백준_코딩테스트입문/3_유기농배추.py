# https://www.acmicpc.net/problem/1012
'''
1번줄: 배추밭 가로길이 M, 세로길이 N, 배추가 심어져 있는 K
2번줄: 배추 좌표 X, Y
배추가 겹치는 경우는 없다

2 <= 테스트 케이스
10 <= 밭 가로길이  8<= 세로길이 17 <= 배추가 심어져있는 곳 
x y
1(0 0)
2(1 0)
3(1 1)
4(4 2)
5(4 3)
6(4 5)
7(2 4)
8(3 4)
9(7 4)
10(8 4)
11(9 4)
12(7 5)
13(8 5)
14(9 5)
15(7 6)
16(8 6)
17(9 6)

10 10 1
5 5

'''

from collections import deque

def bfs(grid, x, y, n, m):
    # BFS를 위한 큐 초기화
    queue = deque([(x, y)])
    # 방향 벡터 (상하좌우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # 유효 범위 내에 있고 배추가 심어진 곳이라면 탐색
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))

def 농사():
    t = int(input())  # 테스트 케이스 수
    results = []
    
    for _ in range(t):
        m, n, k = map(int, input().split())  # 가로, 세로, 배추 위치 개수
        grid = [[0] * m for _ in range(n)]  # 배추밭 초기화
        
        for _ in range(k):
            x, y = map(int, input().split())
            grid[y][x] = 1  # 배추 위치 표시 (x, y는 격자 좌표)
        
        배추흰나비 = 0  # 필요한 지렁이 수
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # 배추가 심어진 곳에서 BFS 시작
                    bfs(grid, i, j, n, m)
                    배추흰나비 += 1
        
        results.append(배추흰나비)
    
    # 결과 출력
    for result in results:
        print(result)

# 실행
농사()
