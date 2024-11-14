
####### for문, range #######################
# n = 3
# s = "Hello"
# arr = [1, 2, 3]


# for 변수 in iterable 객체
# 1. iterable 객체에서 요소를 1개씩 꺼내와 변수에 저장
# 2. for문에 반복
# 3. 꺼내올 iterable 이 없다면? for문을 종료하고 다음 코드를 진행

# range 함수를 사용해서 0 부터 n-1 을 출력하기
# range(start,end,step) : step을 안적을 경우 기본값 1
# range(n) = n번 반복해라 
# for i in range(n):
#     print(i)

# 문자열 for 문 순회: 문자열 s의 문자를 하나씩 출력하기
# for c in s:
#     print(c)

# 리스트 for 문 순회: 리스트 arr의 원소를 하나씩 출력하기
# for x in arr:
#     print(x)


####### break, continue #######################

# s = "Hello"
# for c in s:
#     # 순회 중 변수 c의 값이 알파벳 l 이라면 멈추자!
#     if c == "e":
#         # continue #건너뛰고 다음 반복을 실행해줘
#         break #여기 까지만 실행하고 for문을 나가줘
#     print(c)


###### while문 #################################

# n = 0
# # n이 3보다 작을 때까지 while 문 내용을 수행하자!
# while n < 3: #조건문이 true면 실행해라, 언제까지? 조건문이 false가 될 때 까지
#     print('n =', n)
#     n += 1


# 실습예제 문제1: 구구단 2단 출력하기

# 2 * 1 부터 2 * 9 까지 출력
# 출력 양식: 0 * 0 = 0

# for i in range(1,10):
    # f string 포맷 사용방법 f"{표현식 사용, 변수:포맷 형식으로도 사용 가능}"
    # = 을 사용하여 변수 이름과 값을 출력할 수 있다
    
    # print(f"2 * {i} = {2 * i}")
    
# 하나의 단은 2 * 1 부터 2 * 9 까지 출력하고 2단부터 9단까지 출력
# 출력 양식
# --- 2단 ---
# 0 * 0 = 0

단 = 2
for i in range(1,9):
# 단 증가
    print(f"========{단}단==============")
    for j in range(1,10):
        print(f"{단} * {j} = {단 * j}")
    단 += 1