# https://www.acmicpc.net/problem/1388
'''
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 
형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 
나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 
방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 
만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.



입력
첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 
둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 
이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. 
N과 M은 50 이하인 자연수이다.

-||--||-- => 7 
--||--||- => 5
|--||--|| => 6
||--||--| => 5
-||--||-- => 5
--||--||- => 5


먼저 체크 한것은 카운트X
| = 현재 열과 아래 열 동일한 위치의[X] 값이 같을 경우 True 처리 후 count +1
- = 같은 열 현제 행의 옆칸이 동일 할 경우 True count +1

이게 조건인데 2개 이상의 행(|)이 동일하면 어떻게 할것인가?
ㄴ> 1. -이 나올때 까지 탐색 후 -을 만나면 멈추고 탐색한 열들 다 True 처리 후 True 처리를 한다
-도 마찬가지
 
'''
from collections import deque

def search_patterns(N, M, board):
    # 방문 여부를 기록할 배열
    searched = [[False] * M for _ in range(N)]
    count = 0  # 나무 판자의 개수

    # 탐색 함수 (BFS)
    def bfs(x, y):
        queue = deque([(x, y)])
        searched[x][y] = True  # 현재 위치 방문 처리
        pattern = board[x][y]  # 현재 패턴 ('-' 또는 '|')

        # 탐색 방향 결정
        directions = [(0, 1)] if pattern == '-' else [(1, 0)]  # 가로: 오른쪽, 세로: 아래

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                # 범위 내에 있고, 같은 패턴이며, 아직 방문하지 않은 경우 탐색
            
                if 0 <= nx < N and 0 <= ny < M and not searched[nx][ny] and board[nx][ny] == pattern:
                    searched[nx][ny] = True
                    queue.append((nx, ny))

    # 모든 칸 탐색
    for i in range(N):
        for j in range(M):
            if not searched[i][j]:  # 방문하지 않은 경우만 탐색
                bfs(i, j)
                count += 1  # 새로운 나무 판자를 발견했으므로 증가

    return count

# 입력 처리
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]  # 한 줄씩 입력받기

# 결과 출력
print(search_patterns(N, M, board))
