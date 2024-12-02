'''
https://www.acmicpc.net/problem/11557


문제: 
근처에 있는 학교 중 어느 학교가 술을 가장 많이 먹는지
학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력

2 ===> 테스트 케이스

1test
_____________________________________________
3 ===> 학교 수
Yonsei 10
Korea 10000000
Ewha 20

2test
_____________________________________________
2 ==> 지난해 동안 소비한 술
Yonsei 1
Korea 10000000

[출력]
Korea
Korea


[예제입력1]
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000

[예제출력1]
Korea
Korea

'''
import sys
input = sys.stdin.read
data = input().strip().split("\n")

# 테스트 케이스 수
T = int(data[0])
index = 1  # 현재 처리 중인 데이터 위치

# 결과 저장
results = []

# 한 번의 반복으로 모든 테스트 케이스 처리
while index < len(data):
    N = int(data[index])  # 학교 수
    index += 1

    # 현재 테스트 케이스의 데이터만 슬라이싱
    case_data = data[index:index + N]
    index += N

    # 가장 술 소비가 많은 학교 찾기
    # case_data에서 가장 큰 값을 가진 요소를 찾고 학교 이름을 추출
    max_school = max(case_data, key=lambda line: int(line.split()[1])).split()[0]
    results.append(max_school)

# 결과 출력
print("\n".join(results))
