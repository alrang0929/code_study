# https://www.acmicpc.net/problem/9934
'''
1. 가장 처음에 상근이는 트리의 루트에 있는 빌딩 앞에 서있다.
.2 현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동한다.
3. 현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면, 현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
4. 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동한다.
5. 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동한다.

문제 분석
1. 깊이=k인 완전 이진 트리를 구성해야됨. 
2. 입력으로 주어진 방문 순서는 중위 순회 방식으로 각 노드 방문
3. 주어진 중위 순회 결과를 바탕으로 트리를 구성, 각 레벨별 노드 번호 출력


접근 방법:
1. 트리 구성 이해: 방문할 빌딩 번호를 바탕으로 이진 트리 구성
2. 트리의 분할 정복:
중위 순회 결과를 이용해 트리를 구성하는 재귀적인 방법을 사용
3. 레벨별 노드 수집: 트리를 구성한 후 각 레벨의 노드를 저장, 출력

'''

import sys
input = sys.stdin.read
data = input().split()

# K 값과 빌딩 번호들을 입력으로 받습니다.
K = int(data[0])
building_order = list(map(int, data[1:]))

# 트리를 구성하는 함수
def build_tree(order, depth, levels):
    if not order:
        return
    
    mid = len(order) // 2
    levels[depth].append(order[mid])
    
    # 왼쪽 자식 부분 트리
    build_tree(order[:mid], depth + 1, levels)
    # 오른쪽 자식 부분 트리
    build_tree(order[mid + 1:], depth + 1, levels)

# 각 레벨의 빌딩 번호를 저장할 리스트를 준비합니다.
levels = [[] for _ in range(K)]

# 트리 생성 (재귀적 분할)
build_tree(building_order, 0, levels)

# 결과 출력
for level in levels:
    print(" ".join(map(str, level)))
