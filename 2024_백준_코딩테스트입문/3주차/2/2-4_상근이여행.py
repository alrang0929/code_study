# https://www.acmicpc.net/problem/9372
'''
최소 신장 트리(MST) 개념을 이용해야됨.
주어진 그래프가 항상 연결 그래프 => 모든 국가를 연결하는데 필요한 최소 간선의 수는 (노드 수 -1)


문제 분석:
1. 그래프의 특징
- 국가(노드) = N개
비행기의 종류(간선) = ㅡ
주어진 그래프는 항상 연결 그래프
    ㄴ 즉 모든 노드는 간선들을 통해 서로 연결되어 있음
2. 최소 비행기 개수
    - 모든 국가를 여행하기 위해 최소한으로 필요한 비행기(간선)의 수를 구한다
    - 최소 신장 트리에서는 (노드수 - 1)개의 간선만 있으면 모든 노드를 연결할 수 있음
    
연결 그래프에서, N개의 노드를 모두 연결하기 위해 필요한 간선의 최소 개수는 항상 N - 1
=> 국가의 수 N을 입력받은 후 항상 N - 1을 출력

'''

def min_flights():
    T = int(input())  # 테스트 케이스 수
    results = []
    
    for _ in range(T):
        N, M = map(int, input().split())  # 국가 수 N, 비행기 수 M
        for __ in range(M):  # M개의 간선 입력 (사용하지 않음)
            input()
        # 최소 간선 수는 N - 1
        results.append(N - 1)
    
    # 결과 출력
    for result in results:
        print(result)

# 함수 실행
min_flights()
