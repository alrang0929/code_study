#https://www.acmicpc.net/problem/18352
'''
문제 분석:
- 1 ~ N번까지의 도시, M개의 단방향도로(도로의 거리는 1)
- 특정도시 X에서 출발하여 도달할 수 있는 모든 도시중에서 최단 거리가 정확하게 K인
  모든 도시들의 번호를 출력!!
  (X-> X 최단 거리는 항상 0)
- 입력
    1. 첫째 줄 : 도시의 개수 N, 도로의 개수 M, 거리정보 K, 출발도시 번호 X
    2. ~ M개의 줄: A B(공백으로 구분, A->B 단방향 도로)
- 출력
    : X에서 출발해서 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를
    한 줄에 하나씩 오름차순으로 출력
    (도달할 수 있는 도시 중에서 최단 거리 k인 도시가 하나도 존재하지 X : -1을 출력)

문제 접근: BFS
- 입력
    1. 첫째 줄(공백 구분)
        - N : 도시 수(Node)
        - M : 도로 수(Edge)
        - K : 거리 정보 (route edges)
        - X : 출발 도시 번호(=시작노드)
    2. M개의 줄(공백 구분)
        - A B : A -> B 로가는 Edge를 나타냄.*args
        => for문(M) => map, int, input
- 탐색(bfs)
    1. graph를 인접리스트 형태로 담아주기
     => for문 : 인덱스를 맞춰야 하니까 크기는 N+1
     => A -> B 간선만 반영
    2. route 배열 : 거리정보를 저장
     => 초기에 방문하지 않은 노드들 = -1 초기화
     => 시작 도시 X = 0
    3. 큐를 돌리기!!
        - 시작도시 X를 큐에 추가하면서 탐색.
        - 도시를 하나씩 꺼내서 인접도시를 확인(탐색)
            (if문 -> 아직 방문하지 않은 도시만을 탐색! route[i] == -1)
        - 탐색한 도시는 route값을 갱신. +1,+1, +1,,,
    4. 탐색 끝 => route배열에 각 도시의 최단 거리가 저장이 됩니다.
    5. 거리가 K인 도시들을 result에 추가
        (result가 비어있으면 -1출력, 있으면 도시번호를 출력)

해결 방법:



'''
#코드
#입력처리
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

route = [-1] * (n+1)
route[x]=0

#탐색
def bfs (n, m, k, x):
    queue = deque([x])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if route[i] == -1:
                route[i] = route[node] + 1
                queue.append(i)
#함수실행
bfs(n, m, k, x)
#route중에 k인 애들만 담아주기
# [-1, 0, 1, 3, 4, 5] k == 3
result = [i for i in range(1, n + 1) if route[i] == k]
#출력
#result값이 있는지 없는지 (도시번호 / -1)
if result:
    print('\n'.join(map(str, result)))
else: 
    print(-1)
