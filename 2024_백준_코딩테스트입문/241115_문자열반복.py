'''
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.


2
3 ABC
5 /HTP

AAABBBCCC
/////HHHHHTTTTTPPPPP
'''

# 문제풀이
# 1. 들어오는 문자열을 1글자씩 자른다
# 2. 변환 후 다시 합쳐줄 빈 변수 선언
# 3. 자른 문자열 길이만큼 for문을 돌린다
# 4. for문 안에서 if문을 통해 A=H, B=T, C=P 로 변환 후 빈 변수에 담는다
# 5. 빈 변수를 출력한다


# 1. 테스트 케이스를 받아옴
T = int(input())
# 2. 변환할 문자열을 담을 빈 문자열 준비
P = ""
# 3. T만큼 for문을 돌아준다
for _ in range(T): 
    # 4. R은 반복횟수 / S: 문자열
    R, S = input().split() # R과 S 입력, 3 ABC로 들어오므로 쪼개준다
    R = int(R) # R을 정수형으로 변환
    list_S = list(S) #문자열을 인덱스 단위로 쪼갠다

    # 5. 쪼갠 문자열을 꺼내온다
    for item in list_S:
        # R만큼
        repeat_item = item*R
        # 그리고 P에 값을 쌓아준다
        P += repeat_item 
# 6. 출력을 한다, 마지막에 줄바꿈 방지
print(P, end='')