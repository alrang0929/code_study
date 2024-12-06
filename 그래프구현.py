# 입력 : N, M, V ->  정점의 개수, 간선의 개수, 시작하는 정점
#       다음 M 줄 간선 정보 들어옴

# 로직 :  주어진 간선리스트를 통해서, DFS 와 BFS 로 구현하고
#            간선리스트로는 DFS BFS 는 힘드니까
#            -> 인접행렬로 변경
#            DFS 함수구현 (스택 / 재귀 )
#            BFS 함수구현

# 출력 :   DFS 로 탐색할때, 노드 순차적 출력 ( 한줄 내리고)
#         BFS 로 탐색할때, 노드 순차적 출력


# 입력
N, M, V = map(int, input().split())

# 간선리스트(input) - > 인접행렬 
graph = [[0] *(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 처리 담을 리스트
visited_dfs = [0]* (N+1)
visited_bfs = [0]* (N+1)

# 결과 출력

print(*dfs_스택(V))   # [ 1, 2, 3, 4 ]-> "1 2 3 4"
print(*bfs_큐(V))


# DFS  재귀
def dfs_재귀(V) :
    visited_dfs[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1) :
        if graph[V][i] == 1 and visited_dfs[i] =0 :
            dfs_재귀(i)


# DFS 스택
def dfs_스택(V):
    stack =[V]
    result = []
    while stack :
        node = stack.pop()
        if visted_dfs[node] == 0:
            visted_dfs[node] = 1
            result.append(node)
            
            for i in range(N, 0, -1) :
                if graph[node][i] == 1 and visited_dfs[i] = 0:
                    stack.append(i)
    return result                    

# BFS 큐
def bfs_큐(V):
    queue = [V]
    result = []
    visited_bfs[V] = 1
    
    while queue : 
        node = queue.pop(0)
        result.append(node)
        
        for i in range(1, N+1):
            if graph[node][i] == 1 and visited_bfs[i] = 0:
                    queue.append(i)
                    visited_bfs[i] = 1
    return result    


# sys.setrecursionlimit(10**6) 재귀함수 용량 늘리기