
'''
문제 목적:
BFS를 사용하여 쩰리가 목표 지점까지 도달할 수 있는지를 판별

쩰리가 이동 가능한 방향: 오른쪽 아래

문제 접근 방법:
1. 그래프 모델링: N*N크기의 2차원 배열 표현
- 각 칸에는 이동할 수 있는 "점프 칸 수"가 적혀있음
- 특정 칸에서 오른쪽 or 아래 쪽으로만 이동 가능(이동 거리 = 칸에 적혀 있는 숫자)

2. 목표 조건
- 쩰리가 도달해야 하는 칸은 오른쪽 아래 칸(적혀 있는 숫자: -1)
- 쩰리가 이 칸에 도달할 수 있는지를 판단

3. 그래프 탐색
- 각 칸 = 노드, 이동 가능한 칸 = 간선
- BFS(너비 우선 탐색) or DFS(깊이 우선 탐색)을 사용하여 목표 지점에 도달 가능여부 탐색

4. 중단 조건
- 탐색 중 -1(목표 지점)을 만나면 즉시 탐색 종료 => "HaruHaru" 출력
- 모든 가능 경로를 탐색했지만 도달X => "Hing"

[입력 예제]
3
 1 1 10
1 5 1
2 2 -1



알고리즘
1. 입력처리
- 게임판 크기 N과 N*N크기의 배열을 입력받는다

2. 탐색 초기화:
- BFS를 사용할 경우, 큐(queue)를 초기화하고 출발점(0,0)을 추가
- 방문 여부를 확인하기 위해 visited 배열 사용

3. BFS 탐색:
- 큐에서 현재 위치를 꺼냄
- 현재 칸에 적혀있는 숫자 확인
- 오른쪽 또는 아래로 이동 가능한 칸 계산
- 이동 가능한 칸 유효+방문하지 않은 칸 = queue에 추가
- 이동 중 목표 지점(-1)을 만나면 => 탐색 종료 "HaruHaru" 출력

4. 결과 출력
- 큐가 비었음에도 목표지점에 도달X => "Hing" 출력


함수 선언(can_reach_goal): queue를 이용해 BFS를 수행
- 현재 위치에서 점프 거리만큼 이동할 수 있는 위치를 큐에 추가
- visited 배열을 통해 방문여부 관리 (이전 위치 재방문을 막기 위함)


'''
#1. Queue 구현을 위한 deque import
from collections import deque

#2. queue를 이용해 BFS를 수행할 함수 선언
def can_reach_goal(N, board):
    
    queue = deque([(0,0)])
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        jump = board[x][y]
        if board[x][y] == -1:
            return "HaruHaru"
        if jump == 0:
            continue
        for row_move, col_move in [(0, jump), (jump, 0)]: #x, y의 구분
            new_row, new_col = x + row_move, y + col_move
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
              visited[new_row][new_col] = True
              queue.append((new_row, new_col))
    return "Hing"
    
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = can_reach_goal(N, board)
print(result)

# 시작시간: 5:00 / 풀이완성: 5:20