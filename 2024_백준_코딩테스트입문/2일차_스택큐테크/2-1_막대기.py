'''
[문제]

아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

[입력]
첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고 이어지는 N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

[예제 입력1]
6
6
9
7
6
4
6

[예제 출력1]
3

'''
import sys
sys.stdin = open("input.txt","r")

def count_visible_rods(n, heights):
    stack = []  # 스택 초기화
    visible_count = 0  # 보이는 막대기 개수

    # 오른쪽에서 왼쪽으로 순회
    for height in reversed(heights):
        # 스택의 꼭대기에 있는 막대기가 현재 막대기보다 작으면 제거
        while stack and stack[-1] <= height:
            stack.pop()
        
        # 현재 막대기는 항상 보이므로 스택에 추가
        stack.append(height)
        visible_count += 1

    return visible_count

# 입력 처리
n = int(input())  # 막대기의 개수
heights = [int(input()) for _ in range(n)]  # 막대기의 높이 리스트

# 결과 출력
print(count_visible_rods(n, heights))
