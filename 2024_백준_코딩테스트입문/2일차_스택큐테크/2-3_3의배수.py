
'''
[요구사항]
1. 첫째 줄에 큰 자연수 X
2. X의 각 자리의 숫자 합을 Y
3. Y가 3의 배수 -> X도 3의 배수

- 입력값 : X
- 출력값
    1. 첫째 줄 : Y가 한 자리수가 나올 때까지 몇 번 과정을 거쳤는지
    2. 둘째 줄 : 3의 배수면 "YES",아니면 "NO"

[문제 해결 과정]
0. 함수로 묶어서 해결하려고 합니다 def 
1. 입력값을 받는 변수 X (원래의 큰 자연수)
3. 실행횟수를 나타내는 변수 count

2. Y를 한 자리수로 만들어주는 과정이 필요
    2-0. map과 while문을 활용할 예정
    2-1.X가 str형으로 들어올테니
    2-2. X의 길이가 1 이상이라면 (while문)
        - map으로 X의 요소 str(X)를 int로 변환하고
        - sum으로 감싸서 요소들의 합을 도출하고
        - str형으로 다시 변환해주고,
        - X에 재할당
        - count는 1이 증가

3. print(count)
4. print는 "YES" if int(X) %3 == 0  else "NO"
5. 함수실행
'''
# 정수를 저장할 x
def result():
    x = input()
    # count 누적할 변수
    count = 0

    # 1. 무한 반복으로 받아온 문자열을 1자리수로 쪼개기
    # for i in str(x):
    #     x += i
    # count += 1
        
    
    while len(x) > 1 :
        # 1-2 int로 변환 후 sum으로 합
        # 1-3 문자형으로 변환하여 다시 X에 넣기
        x = str(sum(map(int, x)))
        # 1-4 count =+1
        count += 1

# 2. print 에서 count 출력
    print(count)
# 2-1. print에서 3을 나눴을때 나머지값이 0 이면 "YES" OR "NO"
    print("YES" if int(x) %3 == 0  else "NO")

# 3. 함수실행
result()

# 시작시간: 7:30 / 종료시간: 7:47