# https://www.acmicpc.net/problem/16173
'''
문제 목적:
 BFS 또는 DFS를 사용하여 쩰리가 목표 지점(오른쪽 아래)까지 도달할 수 있는지를 판별

문제 접근 방법:
1. 그래프 모델링: N*M크기의 2차원 배열 표현
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
# 전달받을 인자: N, board
# N = 게임판의 범위를 체크하거나 반복문을 사용할 때 필요
# board 

def can_reach_goal(N, board):
    #1. BFS를 위한 큐 초기화
    queue = deque([(0, 0)])  # 시작점: (0, 0)
    #2. 방문 여부 체크 배열 생성: BFS탐색 과정 중 같은 좌표가 추가되는 것을 방지
    visited = [[False] * N for _ in range(N)]  
    '''
    visited = [[False, False, False],
              [False, False, False],
              [False, False, False]]
    '''
    # 3. 시작점 방문 처리
    visited[0][0] = True
    '''
    visited = [[True, False, False], 
              [False, False, False],
              [False, False, False]]
    '''
    # 2. queue가 true일 경우 반복
    while queue:

        # 1. 입력값 세팅
        # 1) queue가 비어 있지 않은 동안 다음 칸을 계속 탐색
        # 큐의 FIFO를 이용하기 위한 popleft()로 이동카드 꺼내기
        x, y = queue.popleft()
        # 2)현재 칸의 점프 거리 저장
        jump = board[x][y]

        # 2. 예외처리
        # 예외처리 1: 목표지점 도달했을 때
        if board[x][y] == -1: 
            return 'HaruHaru'
        # 예외처리 2: 이동할 수 없는 칸 스킵
        if jump == 0:
            continue
        
        # 3. 게임 진행: 이동할 수 있는 두 방향 (오른쪽, 아래)
        for row_move, col_move in [(0, jump), (jump, 0)]:
            new_row, new_col = x + row_move, y + col_move
            '''
            결과예시:
            1) 새로운 좌표 생성
            new_row = current_row + row_move = 0 + 0 = 0
            new_col = current_col + col_move = 0 + 1 = 1

            2) 결과
            (new_row, new_col) = (0, 1)
            '''
            # 새 좌표가 행의 범위를 벗어나지 않음 그리고 열의 범위도 벗어나지 않음
            # 또 방문한 곳이 아님
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
                # 방문 지점 체크
                visited[new_row][new_col] = True
                # 새로운 위치 저장
                queue.append((new_row, new_col))
    
    return "Hing"  # 모든 탐색을 마쳤으나 도달하지 못함

#3. 입력받기 N, board
N = int(input())
# 보드 생성: N개의 행으로 데이터 전처리 하여 배열 생성
board = [list(map(int, input().split())) for _ in range(N)]

#결과값 받을 변수
result = can_reach_goal(N, board)

#4. 결과 출력 
print(result)
