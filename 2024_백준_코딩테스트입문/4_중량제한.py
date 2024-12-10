# https://www.acmicpc.net/problem/1939
'''
섬 = node
다리 = 간선
주어진 두 공장이 위치한 섬 사이에 가장 큰 중량 제한을 가진 경로를 찾기

중량 제한을 기준으로 가장 큰 제한을 유지할 수 있는 경로
=>두 공장 사이에 가장 큰 중량제한을 가진 경로를 찾는 것


유니온 파인드의 동작 과정:

1. 초기화: 
- 각 원소는 자기 자신을 대표로 가짐, 모든 원소가 독립된 집합을 형성

2. find
- 재귀적으로 부모를 따라가며 최상위 대표 찾기

3. Union:
- 두 집합의 대표 원소를 찾아 한쪽 집합을 다른 쪽에 병합
- Rank나 Size를 기준으로 트리를 병합하여 깊이를 최소화

'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # 랭크에 따라 트리를 합침
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def max_weight(n, m, bridges, start, end):
    # 유니온 파인드 초기화
    uf = UnionFind(n)
    
    # 중량제한을 내림차순으로 정렬
    bridges.sort(key=lambda x: -x[2])  # (A, B, C)에서 C에 대해 내림차순 정렬
    
    # 다리들을 중량제한 순으로 연결
    for a, b, c in bridges:
        uf.union(a-1, b-1)  # 0-based index 사용
        
        # 시작 섬과 끝 섬이 연결되면, 그때의 중량 제한을 반환
        if uf.find(start-1) == uf.find(end-1):
            return c
    
    return -1  # 연결되지 않으면 -1 (이 문제에서는 항상 연결됨)

# 입력 처리
n, m = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

# 결과 출력
print(max_weight(n, m, bridges, start, end))
