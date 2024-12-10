# https://www.acmicpc.net/problem/2108

'''
N은 홀수

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

출력조건:
1번 줄: 산술평균, 소수점 이하 첫째 자리에서 반올림
2번째 줄: 중앙값
3번째 줄: 최빈값, 여러 개일 경우 최빈값 중 두번째로 작은 값 출력
4번째 줄: 범위 출력

'''
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input().strip()) for _ in range(n)]

# 1. 산술평균
산술평균 = round(sum(num_list) / n)

# 2. 중앙값
num_list.sort()
중앙값 = num_list[n // 2]

# 3. 최빈값
frequency = Counter(num_list)
most_common = frequency.most_common()
most_common.sort(key=lambda x: (-x[1], x[0]))  # 빈도수 내림차순, 값 오름차순 정렬

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    최빈값 = most_common[1][0]
else:
    최빈값 = most_common[0][0]

# 4. 범위
범위 = num_list[-1] - num_list[0]

print(산술평균)
print(중앙값)
print(최빈값)
print(범위)