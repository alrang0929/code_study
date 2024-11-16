import sys
sys.stdin = open('input.txt','r')

#주의 개수
n = int(input())
# 근무시간 저장하는 딕셔너리
time_dict = {}

# 근무시간 배열 생성
'''
8:00 ~ 12:00 = 4
12:00 ~ 18:00 = 6
18:00 ~22:00 = 4
22:00 ~ 08:00 = 10
'''
work_time = [4,6,4,10]

for _ in range(n):
    for shift in range(len(work_time)):
        shifts = input().split() # 각 시간대 근무자 명단
        for person in shifts: 
            if person != "-":#사람이 있다면 진행
                if person not in time_dict:
                    # print(person)
                    time_dict[person] = 0 #근무시간 초기화
                time_dict[person] += work_time[shift] #근무자 추가
                # print(time_dict)

# 근무하지 않았을 경우 공평
if len(time_dict)==0 : 
    print("Yes")
else:
    max_time = max(time_dict.values())
    min_time = min(time_dict.values())
    if max_time - min_time <= 12: #공평한 근무시간차 기준이 12시간 이하
        print("Yes")
    else: print("No")