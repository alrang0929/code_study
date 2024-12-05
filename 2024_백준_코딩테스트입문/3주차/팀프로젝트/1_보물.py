# https://www.acmicpc.net/problem/1026

"""
S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 

단, B에 있는 수는 재배열하면 안 된다.

**S의 최솟값**을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 
셋째 줄에는 B에 있는 수가 순서대로 주어진다. 

N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.
"""

# 최소값을 만들기 위해서 배열을 재배열을 해야 하는 상황

# A는 B[i]가 클수록 A[i]는 작게 만들어서
# 그 곱의 합을 최소화 하기 위해서 내림차순으로 정렬

# B는 큰 B[i] 작은 A[i]가 곱해져서
# 최소값을 만들 수 있기 때문에 오름차순 정렬

# 따라서

# --------------------------------
# A는 내림차순으로 정렬
# B는 오름차순으로 정렬
# 인덱스는 0번부터 N-1번까지 곱해주면
# 최소값을 구할 수 있다


# 변수는
# N
# A, B
# S
'''
5 => N
1 1 1 6 0 => A
2 7 8 3 1 => B

'''

import sys
input = sys.stdin.readline
data = input().strip().split('\n')

N = int(data[0])
A = sorted(list(map(int, input().split())), reverse = True) #N log N
B = sorted(list(map(int, input().split()))) #N log N
S = 0
for i in range(N):
    S += A[i]*B[i]
    
print(S)

# 전체 시간복잡도: O(n log n)
# 시작시간: 7:17 풀이완료: 7:38