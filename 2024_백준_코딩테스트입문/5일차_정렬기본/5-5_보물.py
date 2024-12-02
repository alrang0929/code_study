'''
https://www.acmicpc.net/problem/1026

배열A*배열B = 최소값

5
1 1 1 6 0
2 7 8 3 1
'''

# 입력 받기
N = int(input())  # 배열의 길이
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# 배열 정렬
A.sort()  # A는 오름차순 정렬
B.sort(reverse=True)  # B는 내림차순 정렬

# S 값 계산
S = sum(a * b for a, b in zip(A, B)) #zip의 결과: [(0, 8), (1, 7), (1, 3), (1, 2), (6, 1)] << for문 생략하고 진행 가능
# zip(): A와 B의 각 요소를 같은 인덱스끼리 묶어 튜플로 만듦

# 결과 출력
print(S)
