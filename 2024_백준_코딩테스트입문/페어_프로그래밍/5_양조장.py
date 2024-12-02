'''
https://www.acmicpc.net/problem/11557

# 문제 분석
# 첫번째 줄에 테스트 케이스의 수를 입력받고
# 그 테스트 케이스의 횟수만큼 입력을 받는다
# 입력받을 테스트케이스의 첫번째 줄에는 학교의 숫자 n이 들어가고
# n만큼 대학명과 술 소비량을 차례로 작성한다
'''

import sys
# step1. 테스트케이스 입력 받기
T = int(sys.stdin.readline())

# step2. 테스트케이스만큼 반복문
for _ in range(T):
     # step 3. 학교 수
    school_num = int(sys.stdin.readline())

    # step4. 학교명과 술소비량을 담을 딕셔너리 선언
    shljangee = {}
    # step7. 각 테스트 케이스 별로 결과를 출력하기 위해서 내부에 있는 for문 위에 변수를 초기화 해주고
    max = 0
    max_name = ""
    
    for _ in range(school_num): #O(n*school_num)
        # step5. 학교명과 술소비량 입력받기
        name, drink = sys.stdin.readline().split()
        #defaultdict을 사용해서 분기처리 안해도 됨 
        if name not in shljangee :
            shljangee[name] = int(drink)
        else:
            shljangee[name] += int(drink)
        
        # max메서드 사용 가능
        # max_key = max(dict, key=dict.get)
        if shljangee[name] > max:
            max = shljangee[name]
            max_name = name
        
    # print(max_key)
    print(max_name)

