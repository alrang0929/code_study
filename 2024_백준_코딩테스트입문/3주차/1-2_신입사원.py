# https://www.acmicpc.net/problem/1946
'''
2 <== 테스트 케이스
5 <= 지원자 수 
a b
3 2 < = 기준
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1


1. 기준값의 a,b 값기준으로 비교
2. a, b중 하나라도 크다면 합격

'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]) # 서류를 기준으로 정렬
    cnt = 1
    second_rank = rank[0][1]
    for i in range(1,N):
        if rank[i][1] < second_rank: # 면접 순위가 이전사람들보다 높으면
            cnt += 1 # 횟수 증가
            second_rank = rank[i][1]
    print(cnt)