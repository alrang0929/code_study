# https://www.acmicpc.net/problem/3187
'''
문제파악:
1. 울타리는 넘어갈 수 없다.
2. 4방향으로만 움직일 수 있다.
3. 양>=늑대 = 늑대가 모두 잡아먹힘, 양<=늑대: 양이 모두 잡아먹힘
4. 같은 울타리 영역안의 늑대와 양의 숫자를 비교
    
중요조건:
    입력 :
    행과 열을 입력 받고
    받아온 행열의 개수에 맞게 입력

    v는 늑대를 의미, k는 양을 의미, 
    .는 빈공간을 의미, #는 울타리를 의미함

해결방법:
    재귀 -> 런타임에러 발생
    대체방안 -> bfs

문제접근:

'''

from collections import deque

row, col = map(int, input().split())
area = [list(input()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

# 전체 양과 늑대의 수를 누적할 변수
total_v, total_k = 0, 0
directions = [(1,0),(0,1),(-1,0),(0,-1)]


def 양이냐늑대냐 (x, y):
    Queue = deque([(x,y)])
    visited[x][y] = True

    v, k = 0, 0  # 현재 영역의 늑대(v)와 양(k) 개수
    while Queue:
        cx, cy = Queue.popleft() #o(1)
        
        if area[cx][cy] == 'v':
            v+=1
        elif area[cx][cy] == 'k':
            k+=1
        for dx, dy in directions: #o(n)
            nx, ny = cx + dx, cy+dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and area[nx][ny] != "#":
                visited[nx][ny] = True
                Queue.append((nx,ny)) #o(1)
    return v, k
    
#전체 영역 탐색
for i in range(row): #o(n^2)
    for j in range(col):
        if not visited[i][j] and area[i][j] != "#" and area[i][j] !=".":
            v,k = 양이냐늑대냐(i,j)
            if v >= k:
                total_v += v
            else: total_k += k 

print(total_k, total_v)

# 시작시간 7:00 완료시간 7:30
# 전체 시간복잡도: o(n^2)