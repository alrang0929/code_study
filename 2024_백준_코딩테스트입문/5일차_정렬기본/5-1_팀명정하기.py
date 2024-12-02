'''

https://www.acmicpc.net/problem/28114

[조건]
1. 참가자들 입학 연도/100의 나머지 오름차순 정렬
2. 성의 첫 문자 나열 => 풀이 문제 수 만큼

[예제입력 1]
600 2018 AHN
2000 2019 LEE
6000 2020 OH

[예제 출력 1]
181920
OLA

'''

# 팀원 정보 입력 받기


data = int(input().strip())
members = []
for _ in range(3):
    score, year, name = input().split()
    score = int(score)
    year = int(year)%100
    members.append([score, year, name])

# 1. 입학 연도 기준으로 정렬한 팀명 생성
years_sorted = sorted(member[1] for member in members)
team_year = "".join(map(str, years_sorted))

# 2. 문제 해결 수 기준으로 이름의 첫 글자 정렬한 팀명 생성
members.sort(key=lambda x: -x[0])  # 문제 해결 수 기준 내림차순 정렬
# lambda = 간단한 계산기, ex) x를 2배로 계산해라 lambda x: x * 2
team_name = "".join(member[2][0] for member in members)

# 결과 출력
print(team_year)
print(team_name)

