'''

[문제]
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

[입력]
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.


출력
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.

[예제 입력1]
2 =>해빈이가 가진 의상 수
3 => 해빈이가 가진 의상의 이름 / 종류, 같은 종류의 의상은 하나만 입을 수 있음
hat headgear
sunglasses eyewear
turban headgear

3 => 해빈이가 가진 의상의 이름 / 종류, 같은 종류의 의상은 하나만 입을 수 있음
mask face
sunglasses face
makeup face

[예제 출력1]
5
3

[힌트]
첫 번째 테스트 케이스는 headgear에 해당하는 의상이 hat, turban이며 eyewear에 해당하는 의상이 sunglasses이므로   (hat), (turban), (sunglasses), (hat,sunglasses), (turban,sunglasses)로 총 5가지 이다.

headgear = [hat, turban]
eyewear = [sunglasses]

'''

'''
어떻게 접근해야될까..
조합론을 이용하여 해결할 수 있는 문제
1. 각 의상의 종류별 선택지 확인
2. 의상의 종류별로 선택하지 않은 경우도 포함한 모든 경우의 수 계산
3. 알몸을 제외하고 총 조합의 수 출력


'''

import sys

T = int(sys.stdin.readline().strip())

# 테스트케이스 개수만큼 반복
for _ in range(T): #O(n)
    wears = {}
    n = int(sys.stdin.readline().strip())
    # 의상 개수만큼 반복
    for _ in range(n):  #O(n)
        name, type = sys.stdin.readline().strip().split()
        if type in wears: 
            # 종류가 이미 있으면 해당 종류에 의상 이름만 추가
            wears[type].append(name)
        else:
            # 종류가 사전형에 없으면 추가
            wears[type] = [name]
    
    cnt = 1
    
    # 조합식을 세워 계산
    # +1하는 이유는 알몸도 옷이라고 생각해 추가
    for x in wears:  #O(n)
        cnt *= (len(wears[x]) + 1)
	
    # -1하는 이유 모든 종류의 옷을 착용하지 않았을 경우를 제외
    print(cnt-1)


    # 전체 시간복잡도 #O(n2)