# https://www.acmicpc.net/problem/22252

'''
상황분석:
- 초기 투자를 통해 여러명의 "정보 고릴라"에게 정보 수집
- 정해진 예산을 가지고 정보를 얻을 것
 
 Q = 관찰하면서 얻은 정보
 
 정보 케이스
 Name k: C1, C2, .... Ck : 이름이 [Name]인 고릴라가 k개의 정보를 얻었으며
 각 가치는 C1 부터 Ck 까지
 Name b: 호식이가 이름이 [Nake]인 고릴라에게 구매할 정보 개수
 - 이때 정보 중 가장 비싼 B개를 구매
 - 개수가 b개 이하면 전부 구매
 
 
 7
1 Cpp 5 10 4 2 8 4
1 Java 2 8 2
2 Cpp 2
1 Cpp 2 10 3
2 Cpp 3
2 Java 1
2 Python 10

44

'''

import heapq
from collections import defaultdict

def process_queries(queries):
    gorilla_data = defaultdict(list)  # 고릴라 이름별 정보 저장
    total_value = 0  # 호석이의 정보 구매 총합

    for query in queries:
        parts = query.split()
        q_type = int(parts[0])
        name = parts[1]

        if q_type == 1:
            # 정보 추가
            k = int(parts[2])
            values = map(int, parts[3:])
            for value in values:
                heapq.heappush(gorilla_data[name], -value)  # 최대 힙 (음수로 저장)
        elif q_type == 2:
            # 정보 구매
            b = int(parts[2])
            if name in gorilla_data:
                for _ in range(b):
                    if gorilla_data[name]:  # 고릴라에게 정보가 있으면
                        total_value += -heapq.heappop(gorilla_data[name])  # 음수로 저장된 값을 복원
                    else:
                        break  # 고릴라가 더 이상 정보가 없으면 종료

    return total_value

# 입력 처리
q = int(input())
queries = [input() for _ in range(q)]

# 결과 출력
print(process_queries(queries))
