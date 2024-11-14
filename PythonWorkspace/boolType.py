# # 실수인 경우는?
# # x = 0.1+0.1+0.1
# # print(x == 0.3)#False

# # 이것은 파이썬의 문제.. round를 통해 문제를 해결하도록 하자
# # round : 반올림 매소드.. round(구할놈,몇자리 까지 구할거냐?)
# print("use round function:",round(0.1 + 0.1 + 0.1, 1) == 0.3)#True

# # isclose
# # math : python 내장 모듈
# # isclose : 충분히 가까운 값이면 ㄱㄱ
# from math import isclose
# # isclose : isclose(값, 비교할놈)
# print("use isclose function: " , isclose(0.1 + 0.1 + 0.1, 0.3))



# # decimal module
# from decimal import Decimal
# # Decimal안에 있는 값만 사용해줘
# # 주의: 실수값 자체를 정보를 정답을 하면 실수 자체가 오차가 있기 때문에 false를 반환
# # 그래서 decimal을 할땐 문자열 값으로 전달..
# print("decimal module: ", Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))


""" 

x = True << 예약어

""" 

x = True # 참
y = False # 거짓

# 논리연산자: and or rot
# print(True and False) #양쪽이 true여야 true
print(True or False) #둘중 하나가 true여도 true

# 근데 파이썬이 가진 bool값은 특별함... 단락평가!
'''
파이썬에선 and 연산자를 어떻게 평가하나?

1. 첫번째 값이 true 일 경우
- True and False
- True and "문자열" => 문자열
앞의 값이 true면 우항의 값은 어쨌든 따라옴! 따라서 우항의 값을 반환함

2. or 연산자 : 둘중의 하나가 true여도 true
- 좌항이 False or False 면 false
- 얘도 우항의 값을 그대로 반환
'''

# 문자열 Text Sequence Type (str)
# 인덱스: 구별하기 위한 값, 이걸 하나의 값만 가져오면 indexing, 여러개를 줄지어 데려오면 slicing
# a[선택조건] 으로 가져옴

a = 'hello'
b = "hello"
c = '''hello'''
d = """hello"""

# 인덱싱
print(a[0])

# 슬라이싱 대상[start:end:step(:건너 뛰면서, 생략한다면 기본값 1)]
print(a[0:2]) #he 1을 건너뛴 1번째까지 출력
print(a[0:4:2]) #hl 종료에 다다를 때 까지 0부터 2씩 건너뛰면서 실행
print(a[::-1]) # start 빈값: 처음부터, end빈값: 끝까지, -1 = 역순

# 메소드
'''
-★ `find()` : 문자열에서 특정 문자열의 위치를 찾는다
- ★`replace()` : 문자열에서 특정 문자열을 지정한 문자열로 대체한다
- `upper()` : 대문자로 만든다
- `lower()`: 소문자로 만든다
- ★`join()` : 특정문자로 연결한다
- ★`format()` : 포멧팅 함수
- ★`split()` : 문자열을 특정 구분자를 기준으로 나눈다.

'''

str1 = "hello python"

# find: 내가 찾고자하는 문자열의 인덱스 반환, 없으면 -1
str1.find('p')
# 6

# 문자열중 replace("이놈을 찾아","이걸로 대체")
str1.replace('hello', 'hi')
# hi python

# 대상을 전부 대문자로 바꿔~~~ 
str1.upper()
# HELLO PYTHON

# 대상자를 전부 소문자로 바꿔~
str1.lower()
# hello python

# 
".".join(str1)
#h.e.l.l.o. .p.y.t.h.o.n

# 대상을 기준을 가지고 쪼개버리겠다
str1.split(" ")
# ['hello', 'python']