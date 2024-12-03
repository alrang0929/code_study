'''
https://www.acmicpc.net/problem/1863

도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다. 
스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까? 
건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정한다.

정확히 건물이 몇 개 있는지 알아내는 것은 대부분의 경우에 불가능하고, 
건물이 최소한 몇 채 인지 알아내는 것은 가능해 보인다. 이를 알아내는 프로그램을 작성해 보자.

[입력]
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 50,000) 다음 n개의 줄에는 왼쪽부터 스카이라인을 보아 갈 때 스카이라인의 고도가 바뀌는 
지점의 좌표 x와 y가 주어진다. (1 ≤ x ≤ 1,000,000. 0 ≤ y ≤ 500,000) 첫 번째 지점의 x좌표는 항상 1이다.

[출력]
첫 줄에 최소 건물 개수를 출력한다.

10 <==최소 건물 수 
1 1
2 2
5 1
6 3
8 1
11 0
15 2
17 3
20 2
22 1

6
'''

import sys
input = sys.stdin.read

# 입력 처리
data = input().strip().split("\n")
n = int(data[0])
points = [tuple(map(int, line.split())) for line in data[1:]]

# 변수 초기화
stack = []
building_count = 0

# 스카이라인 처리
for x, y in points:
    # 현재 고도보다 높은 고도를 스택에서 제거
    while stack and stack[-1] > y:
        stack.pop()

    # 새로운 고도 추가 (이전에 없던 고도)
    if not stack or stack[-1] < y:
        if y > 0:  # 고도가 0보다 큰 경우에만 건물 카운트 증가
            building_count += 1
        stack.append(y)

# 결과 출력
print(building_count)
