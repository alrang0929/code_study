# https://www.acmicpc.net/problem/2210
'''
1. 5x5 숫자판에서 시작점과 경로를 자유롭게 정해 6자리 수를 만들어야함
- 이동 경로는 4방, 중복된 경로도 허용 가능
- 가능한 모든 6자리 수를 집합에 저장해 중복 제거 = set

2. DFS 사용
DFS를 사용해 숫자판의 모든 위치에서 시작하여 가능한 모든 경로 탐색
- 현재 위치와 누적된 문자열(현재까지 만든 숫자)를 인자로 재귀적으로 호출
- 탐색 깊이가 6이 되면 경로 탐색을 종료하고 결과를 저장

3. 중복 제거 = set

'''

def unique_six_digit_numbers(board):
    # 중복을 제거하기 위한 set
    results = set()
    # 상하좌우 이동 좌표
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = 5  # 숫자판 크기

    # DFS 정의
    def dfs(x, y, number):
        # 숫자 문자열이 6자리가 되면 결과에 추가
        if len(number) == 6:
            results.add(number)
            return
        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 유효한 좌표인지 확인
            if 0 <= nx < n and 0 <= ny < n:
                dfs(nx, ny, number + board[nx][ny])

    # 숫자판의 모든 위치에서 DFS 시작
    for i in range(n):
        for j in range(n):
            dfs(i, j, board[i][j])

    return len(results)


# 입력 받기
board = [
    input().split()
    for _ in range(5)
]

# 결과 출력
print(unique_six_digit_numbers(board))
