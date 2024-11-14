# 참 / 거짓
# print(5>10) # False
# print(5<10) # True
# print(not True)
# not : 뒤에 있는 값의 반대를 리턴
# print(not (5>10))



# 애완동물을 소개해 주세요~
# 문제: 연탄이가 개명함!! 어떻게 해야되나

animal = "고양이"
name = "해피"
age = 2
hobby = "산책"
is_adult = age >= 3

print("우리집"+ animal +"는" + name +"에요")
# 스트링 형태의 변수를 호출하려면 srt로 감싸 정수형을 문자형으로 바꿔줘야
# 이런식으로 중간에서 값을 변경할 수 있음
hobby = "공놀이"
print(name +"는"+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
#  "+"를 ","로 진행할경우 str변환 없이 그냥 사용 가능, 대신 빈칸이 추가됨
print(name ,"는",age,"살이며, ",hobby,"을 아주 좋아해요")
print(name +"는 어른일까요?"+ str(is_adult))


# 파이썬의 주석
#  < 한줄주석
''' 
이건 여러줄 주석
'''

# 문제: 변수를 이용하여 다음 문장을 출력하시오
# 변수명: station
# 변수값: "사당","신도림","인천공항" 순으로 입력
# 출력문장: XX행 열차가 들어오고 있습니다.

# 역값을 담고 있는 배열
station = ["사당","신도림","인천공항"]
for item in station: print(item+"행 열차가 들어오고 있습니다.")
