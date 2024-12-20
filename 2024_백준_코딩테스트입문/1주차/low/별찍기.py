""" 
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

예제 입력: 5

예제 출력:

*        * << *:1 / 빈칸: 8 / *:1
**      ** << *:2 / 빈칸: 6 / *:2
***    *** << *:3 / 빈칸: 4 / *:3
****  **** << *:4 / 빈칸: 2 / *:4
********** << *:5 / 빈칸: 0 / *:5
****  **** << *:4 / 빈칸: 2 / *:4
***    *** << *:3 / 빈칸: 4 / *:3
**      ** << *:2 / 빈칸: 6 / *:2
*        * << *:1 / 빈칸: 8 / *:1

"""

'''
..뭐 어케 접근해야됨?

1. 예제를 기준으로 생각해보자..
별이 그려지는 줄 수 : 9, 즉 5*2-1

2. 5번째 줄 부터 감소
1번줄 1
2번줄 2
3번줄 3
4번줄 4
5번줄 5
6번줄 4
...

range(start, end, step): 특정 범위를 순회할 때 사용

'''
# N = 5
# # 1부터 N까지 별의 개수 증가해라
for i in range(1, N+1):
    # 별 출력 end="" : 줄바꿈 방지
    print("*"*i, end="")
    # 공백 출력 
    print(" "*(2*(N-i)),end="")
    # 별 출력
    print("*"*i)
    
    # 별 공백 2배수로 나오게 수정!!!
    
# N-1부터 1까지 별의 개수 감소
for i in range(N-1, 0, -1):
    # 별 출력
    print("*" * i, end="")
    # 공백 출력
    print(" "*(2*(N-i)),end="")
    # 별 출력
    print("*" * i)
'''
*         *
**       **
***     ***
****   ****
***** ***** 
****  ****
***    ***
**      **
*        *
    
    
    1차 실패
'''

N = 5
for i in range(1, N+1):
    print("*"*i+" "*(N*2-i*2)+"*"*i)

for j in range(N-1, 0, -1):
    print("*"*j+" "*(N*2-j*2)+"*"*j)


