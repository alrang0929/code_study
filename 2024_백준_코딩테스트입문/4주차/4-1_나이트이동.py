# https://www.acmicpc.net/problem/7562
'''
3 <= 테스트 케이스
========================== case1
8 <= 체스판의 크기
0 0 <= 현재 나이트가 있는 칸
7 0 <= 이동해야하는 칸

========================== case2
100
0 0
30 50

========================== case3
10
1 1
1 1
_______________________________________________
위 케이스를 토대로 생각해보자
case1: 
board: 8x8 격자판
현재 나이트의 위치: (0, 0) (체스판의 가장 왼쪽 위 칸)
이동해야 하는 칸: (7, 0) (체스판의 가장 아래쪽 왼쪽 칸)
=> 나이트가 몇 번 움직여야 (0, 0)에서 (7, 0)으로 도달할 수 있는가

테스트 케이스 활용:
1. 입력값 처리:  체스판 크기, 시작점, 목표점 받기
2. 문제조건 확인
    - 시작점과 목표점이 같냐? 0 출력
3. BFS 탐색 수행(=> 최단 횟수를 알아내야 때문):
    방향 규칙을 따라 나이트를 이동시킴, 목표점에 도달하기 위한 최소 이동 횟수 계산
4. 각 테스트 케이스 결과 저장 및 출력



'''

from collections import deque

# 나이트의 8가지 이동 방향
directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs_min_moves(board_size, start, end):
    if start == end:
        return 0  # 시작점과 목표점이 같으면 이동 필요 없음
    
    # 방문 체크 배열 초기화
    visited = [[False] * board_size for _ in range(board_size)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        # 나이트의 8방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 체스판 범위 내에서만 이동
            if 0 <= nx < board_size and 0 <= ny < board_size and not visited[nx][ny]:
                if (nx, ny) == end:  # 목표점 도달
                    return moves + 1
                
                # 다음 위치를 큐에 추가하고 방문 체크
                queue.append((nx, ny, moves + 1))
                visited[nx][ny] = True

    return -1  # 목표점에 도달하지 못한 경우 (문제 조건상 발생하지 않음)

# 입력 처리
t = int(input())

for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    # 계산 후 즉시 출력
    print(bfs_min_moves(l, start, end))
