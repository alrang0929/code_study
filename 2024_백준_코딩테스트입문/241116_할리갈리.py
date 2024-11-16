import sys
sys.stdin = open('input.txt','r')

'''
할리갈리 규칙:
1. 4가지의 과일(STRAWBERRY, BANANA, LIME, PLUM)이 최대 5개 그려져 있음
2. 카드 뭉치를 [공평]하게 나눠가지고
3. 먼저 다 소모한 사람이 이김
4. 1인 한장씩 출력
5. 정확히 동일한 과일 5개가 있는 경우 종

N = 펼쳐진 카드 개수
S = [과일S, 갯수X]

3
BANANA 2
PLUM 4
BANANA 3



test1: 카드 데이터를 리스트화 하여 조건문으로 비교
카드가 1장만 있을 때의 경우를 설정하지 않아 실행횟수를 초과함

N = int(input()) #펼쳐진 카드 개수
s_list = list() #과일 리스트
x_list = list() #숫자 리스트

# 과일, 숫자 리스트 출력
for i in range(N):
    s,x = input().split() #s = 과일, x 개수
    s_list.append(s)
    x_list.append(int(x))

for i in range(1,N):
    # case 1: 같은 과일의 숫자 합이 10인 경우, 같은 과일에 합이 5를 초과한 경우
    if (s_list[i] == s_list[i-1] and x_list[i]+x_list[i-1] <= 10) or (s_list[i] == s_list[i-1] and x_list[i]+x_list[i-1] >= 5):
         print("No")
    # case 2: 과일은 다른데 하나라도 5개인 경우
    elif s_list[i] != s_list[i-1] and x_list[i] == 5: 
        print("Yes")
    # case 3: 그 외는 ㄴㄴ
    else: print("No")
'''

# test2: 그래서 실시간으로 카드를 비교했더니 
#  LIME 5, LINE 1 케이스에서 에러남..  실시간으로 합산하는 탓에 첫번째에서 YES 값 호출하고 코드 나오는듯..

'''

N = int(input())
fruit_count = {}  # 과일별 개수를 저장할 딕셔너리

for _ in range(N):
    s, x = input().split()
    x = int(x)

    # 과일 개수 업데이트
    if s in fruit_count:
        fruit_count[s] += x
    else:
        fruit_count[s] = x

    # 할리갈리 조건 확인
    if fruit_count[s] == 5:  # 현재 과일이 정확히 5개일 때만 "YES"
        print("YES")
        break
    elif fruit_count[s] > 5:  # 5개 초과 시 바로 "NO" 출력 후 종료
        print("NO")
        break

else:  # 할리갈리가 발생하지 않은 경우
    print("NO")
    
    '''
    
# test3: 전에 푼 근무지옥 처럼 for문 다 돌은 후 외부에서 계산하는걸로..!!
N = int(input())
fruit_count = {}  # 과일별 개수를 저장할 딕셔너리

for _ in range(N):
    s, x = input().split()
    x = int(x)

    # 과일 개수 업데이트
    if s in fruit_count:
        fruit_count[s] += x
    else:
        fruit_count[s] = x


    # 할리갈리 조건 확인
if fruit_count[s] == 5:  # 현재 과일이 정확히 5개일 때만 "YES"
    print("YES")
elif fruit_count[s] > 5:  # 5개 초과 시 바로 "NO" 출력 후 종료
    print("NO")

else:  # 할리갈리가 발생하지 않은 경우
    print("NO")
    
    # 백준에서 제시된 예제는 모두 맞게 출력하나 채점시 틀렸습니다 처리....원인찾아보기