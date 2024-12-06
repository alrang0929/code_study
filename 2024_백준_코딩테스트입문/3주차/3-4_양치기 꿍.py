# https://www.acmicpc.net/problem/3187
'''
문제파악:
울타리 = #로 구분된 각각의 영역에 양(k)와 늑대의 수(v)를 rPtksgodigka
- 같은 영역인 경우: 양>늑대 = 늑대가 모두 잡아먹힘, 양<늑대: 양이 모두 잡아먹힘

핵심: 울타리로 구분된 영역 안에 양과 늑대의 숫자를 비교

중요조건:
- 상하좌우 4방향만 이동 가능
- 울타리(#)로 막힌 구역은 서로 독립적인 영역 형성
- 울타리로 구분되지 않은 빈 공간(.)에는 양, 늑대 없음

해결방법:
- 영역을 탐색하면서 각 구역의 양과 늑대수를 구분해야됨
따라서 DFS or BFS

- 탐색 영역에서 양(k)와 늑대(v)의 개수를 체크
조건에 따라 결과 업데이트

문제접근:
1. 그래프 탐색
BFS를 사용하여 독립된 영역 탐색, 양 늑대 수 체크
- 방문 여부를 기록하기 위해 visited 배열 사용

3. 조건에 따른 처리
- 같은 영역인 경우: 양>늑대 = 늑대가 모두 잡아먹힘, 양<늑대: 양이 모두 잡아먹힘

4. 결과 합산:
모든 영역을 탐색한 후 살아남은 양과 늑대의 총합 출력


*울타리 영역 찾는 과정

1. 초기상태
flelde
...#..
.##v#.
#v.#.#
#.k#.#
.###.#
...###

visited
000000
000000
000000
000000
000000
000000


2. 첫 번째 탐색 시작 ((2, 2)에서 시작)
(2, 2)는 늑대('v')가 위치한 좌표입니다. BFS를 시작
visited[2][2] = True로 설정하고 탐색을 진행

...#..
.##v#.
#v.#.#
#.k#.#
.###.#
...###

000000
000000
001000
000000
000000
000000

3. 상하좌우 탐색(탐색기준 (2,2))
위쪽 ((1, 2)): field[1][2] == '#' → 울타리이므로 이동 불가.
아래쪽 ((3, 2)): field[3][2] == '.' → 이동 가능, 큐에 추가.
왼쪽 ((2, 1)): field[2][1] == 'v' → 늑대, 이동 가능, 큐에 추가.
오른쪽 ((2, 3)): field[2][3] == '#' → 울타리이므로 이동 불가.

4. 두 번째 탐색 (큐에서 (3, 2) 처리)
- (3, 2)를 방문
- visited[3][2] = True

...#..
.##v#.
#v.#.#
#.k#.#
.###.#
...###

000000
000000
001000
001000
000000
000000

6. 네 번째 탐색 (큐에서 (3, 1) 처리)
(3, 1)을 방문합니다. (visited[3][1] = True)

000000
000000
011000
011000
000000
000000

상하좌우 탐색:
    위쪽 ((2, 1)): 이미 방문 → 탐색하지 않음.
    아래쪽 ((4, 1)): field[4][1] == '#' → 울타리이므로 이동 불가.
    왼쪽 ((3, 0)): field[3][0] == '#' → 울타리이므로 이동 불가.
    오른쪽 ((3, 2)): 이미 방문 → 탐색하지 않음.

7. 첫 번째 영역 탐색 종료
- BFS 큐가 비었으므로 (2, 2)에서 시작한 탐색이 끝났습니다.
- 이 탐색으로 확인된 영역은 다음과 같습니다:
    -늑대('v') 2마리, 양('k') 0마리 → 늑대가 살아남음.
    
8. 다음 탐색 시작
아직 방문하지 않은 좌표 (3, 4)로 이동하여 새 BFS 탐색 시작.
위와 같은 방식으로 모든 영역을 탐색합니다

field[nx][ny] != '#'로 울타리를 넘지 않도록 제약적 관리


'''

from collections import deque

# BFS를 이용한 풀이
def count_survivors(R, C, field):
    # 상하좌우 이동을 위한 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * C for _ in range(R)]

    def bfs(x, y):
        # BFS를 통해 하나의 영역 탐색
        queue = deque([(x, y)])
        visited[x][y] = True

        # 양과 늑대의 초기 수
        sheep = 0
        wolf = 0

        # 탐색 시작
        while queue:
            cx, cy = queue.popleft()
            # 현재 위치의 값을 확인
            if field[cx][cy] == 'k':
                sheep += 1
            elif field[cx][cy] == 'v':
                wolf += 1

            # 네 방향 탐색
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                # 유효한 좌표인지 확인 및 방문 여부 체크
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        # 이 영역에서 양과 늑대의 결과 반환
        return sheep, wolf

    # 전체 필드 탐색
    total_sheep = 0
    total_wolf = 0

    for i in range(R):
        for j in range(C):
            # 방문하지 않았고 울타리가 아닌 경우 탐색 시작
            if not visited[i][j] and field[i][j] != '#':
                sheep, wolf = bfs(i, j)
                # 양이 더 많으면 늑대는 모두 잡아먹힘
                if sheep > wolf:
                    total_sheep += sheep
                else:
                    total_wolf += wolf

    return total_sheep, total_wolf

# 입력 처리
R, C = map(int, input().split())
field = [input().strip() for _ in range(R)]

# 결과 계산 및 출력
sheep, wolf = count_survivors(R, C, field)
print(sheep, wolf)
# O(R × C).