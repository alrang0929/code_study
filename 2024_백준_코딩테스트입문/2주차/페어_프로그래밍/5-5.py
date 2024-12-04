import sys
# step1. 테스트케이스 입력 받기
t = int(sys.stdin.readline())
# step2. 테스트케이스만큼 반복문
for _ in range(t):
    # step 3. 학교의 숫자 입력받기
    n = int(sys.stdin.readline())
    # step4. 학교명과 술소비량을 담을 딕셔너리 선언
    univercity ={}
    # step7. 각 테스트 케이스 별로 결과를 출력하기 위해서 내부에 있는 for문 위에 변수를 초기화 해주고
    max_univercity=""
    max_amount=0
    for _ in range(n):
         # step5. 학교명과 술소비량 입력받기
        name,amount = sys.stdin.readline().split()
        # step6. univercity딕셔너리에 name이라는 키가 없다면 amount를 정수로 변환해서 value로 저장해주고, 있다면 해당되는 key value에 amount를 더해주기
        if name not in univercity:
            univercity[name]= int(amount)
        else :
            univercity[name]+=int(amount)
        # 여기까지 완료된 부분은 대학과 술소비량을 짝지어서 딕셔너리에 넣어준 것
        # 남은 부분은 테스트 케이스 별로 소비량이 많은 대학의 이름을 출력하는 것
        # step 8. 여기서 조건
        # 만약 현재 입력받은 대학의 소비량이 max로 저장되어있는 술 소비량 보다 많다면
        # max 변수와 대학이름을 담고 있는 변수에 지금 현재 입력받은 소비량과 대학명을 갱신 시켜주는 것으로
        if int(amount)>max_amount:
            max_amount=int(amount)
            max_univercity= name
    # step9. 내부의 for문을 벗어나서
    # 첫번째 케이스의 입력이 완료가 되면 대학명 출력
    print(max_univercity)