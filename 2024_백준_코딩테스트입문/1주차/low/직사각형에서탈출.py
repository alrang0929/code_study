'''
문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.

제한
1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
x, y, w, h는 정수

'''

# 입력받기
input_data = input()

# 입력된 값을 공백을 기준으로 나누기
x, y, w, h = input_data.split()

# 문자열을 정수로 변환
x = int(x)
y = int(y)
w = int(w)
h = int(h)

# 각 경계까지의 거리 계산
distance_to_left = x
distance_to_bottom = y
distance_to_right = w - x
distance_to_top = h - y

# 최솟값 찾기
min_distance = distance_to_left

if distance_to_bottom < min_distance:
    min_distance = distance_to_bottom

if distance_to_right < min_distance:
    min_distance = distance_to_right

if distance_to_top < min_distance:
    min_distance = distance_to_top

# 결과 출력
print(min_distance)
