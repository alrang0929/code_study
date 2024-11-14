#### 리스트 list #######################
# list는 문자열과 비슷한 성격을 가지고 있음
# 배열형태의 모양을 하고있음


# list  선언하기
# a = list() # 빈 리스트 생성
# b = [] # 빈 리스트 생성
# c = [1, 2, 3] # 1, 2, 3을 원소로 가지는 list 생성

# # 선언한 리스트의 원소는 [] 안에 인덱스를 작성하여 접근할 수 있어요
# print(c[1]) # c의 1번 인덱스, 즉 2가 출력됩니다.


# append / 더하기 +

# a = [] # 빈 리스트 선언
# a.append(3) # a에 3을 추가하자!
# print(a) # [3]

# # Python은 list 간의 덧셈이 지원됩니다 
# b = [1, 2]
# a += b # a의 뒤에 b를 붙이기
# print(a) # [3, 1, 2]
# c = b + a
# print(c) # [1, 2, 3, 1, 2]

# pop
# 리스트의 맨 마지막 워소를 제거하고 그 값을 반환
# a = [1, 2]
# b = a.pop() # 맨 뒤의 원소를 제거하자!
# print(b)  # 2
# print(a)  # [1] => 2가 제거된 걸 확인할 수 있습니다

# # 특정 인덱스 원소를 제거하는 것도 가능
# a = [1, 2, 3]
# b = a.pop(1) # 1번 인덱스의 원소를 제거하자!
# print(b) # 2
# print(a) # [1, 3]


# (value A) to (list B)
# 값 A가 리스트 B안에 있다면 true반환

# arr = [1, 2, 3]
# print(1 in arr) # True
# print(5 in arr) # False
# print("1" in arr) # False -> arr에 문자열 1은 없음!

# set :  중복이 없는 데이터 집합인 구조, 중복값을 제외하고 반환함
# 빈 set 선언하기
# a = set()

# # 원소가 있는 set을 선언하기
# b = {1, 2, 3, 3}

# # 주의: 빈 set를 괄호로 선언하면 딕셔너리가 생성됩니다.
# c = {} # set이 아닌 dictionary!

# # add
# a = set()
# a.add(1)
# print(a) # {1}

# # 중복 원소를 추가해보면?
# a.add(1)
# print(a) # {1}


# #(value A) in (set B)
# arr = {1, 2, 3}
# print(1 in arr) # True
# print(5 in arr) # False
# print("1" in arr) # False -> arr에 문자열 1은 없음!


# #### 딕셔너리 dictionary############
# # key와 value를 이어주는 자료구조, key는 하나의 value만 가질 수 있음
# # 객체랑 비슷한듯? 여기선 index 값으로 key를 사용한다

# # 빈 딕셔너리 생성
# my_dic = {}
# # 신규 key - value 값 지정
# my_dic["key"] = "value"
# # 선언한 딕셔너리의 원소에 접근해 볼게요
# print(my_dic["key"]) # value

# # 같은 key에 다른 value를 지정하면 value가 덮어써집니다
# my_dic["key"] = "value2"
# print(my_dic["key"]) # value2

# # 값이 채워진 딕셔너리로 선언하는 것도 가능해요.
# mapper = {1: "one", 2: "two", 3: "three"}
# print(mapper[2]) # two
# # mapper[] << 무조건 선택하겠다


# # get ################################################

# mapper = {1: "one", 2: "two", 3: "three"}
# print(mapper.get(3)) #key에 맞는 값을 내놔라, 없으면? 예외처리 가능

# mapper = {1: "one", 2: "two", 3: "three"}
# print(mapper.get(4, "No Result!")) # No Result!


#연습문제##########################################
# 1. 주어진 리스트에서 10이상 정수의 합계 구하기
# 출력: 10이상 정수의 합계는 00입니다.
# x = [1, 10, 2, 9, 43, 9, 15]

# sum = 0
# for v in x:
#     if v >=10:sum += v

# print(f"10이상 정수의 합계는 {sum}입니다")

# 2. 최대값 찾기
# 사용자로부터 입력받은 정수 중 최대값을 찾아 출력하시오.
# 입력: 1 4 10 (공백단위로 정수 여러개)
# 출력: 최대값은 10 입니다.
n = "1 4 10"
nums = n.split(' ')
max_num = int(nums[0])
print(max_num)
for num in nums:
    if max_num < int(num):
        max_num = int(num)

# print(f"최대값은 {max_num}입니다.")

# 사용자로부터 입력받은 정수들을 중복을 제거하여 출력하시오.
# 입력: 1 4 4 (공백단위로 정수 여러개)
# 출력: 1 4

num = "1 4 4"
nums = num.split(' ')
num_set = set()

for n in nums:
    # nums로 for문을 돌고 num_set에 item을 추가해서 중복요소 제거
    num_set.add(n)
print(num_set)