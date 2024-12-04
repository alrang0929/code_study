import sys, heapq
input = sys.stdin.readline

# 1. 입력 받기 (n = 거인의 수, h = 센티의 키 , t = 마법망치 사용 횟수)
n, h, t = map(int, input().split())

# 2. 거인들의 키를 음수로 변환하여 리스트에 저장 (최대 힙처럼 사용)
giants = [-int(input()) for _ in range(n)]
# 힙으로 변환
heapq.heapify(giants) # O(n)

# 마법 사용 횟수 변수 초기화 + 누적시킬 변수 선언
count = 0

# O(t = 동일한 숫자 값일 경우 n 으로 치환 가능 // 특정 값인지 체크 ·log n)
# for문, 망치 사용 횟수만큼
for i in range(t): #O(n log n)
    # 현재 가장 큰 거인의 키가 1이거나 센티보다 작은 경우
    max_giants = -giants[0]
    if max_giants == 1 or max_giants < h: #O(1) 루트기 때문에
        # 멈춤
        break
    # 아니면
    else:
        # 가장 큰 거인의 키를 절반으로 줄이고 다시 힙에 저장
        heapq.heapreplace(giants, -(max_giants // 2)) #O(log n)
        # 마법 사용 회수 증가
        count += 1
# 마법을 사용 후 가장 큰 거인의 키가 h보다 크다면
if -giants[0] == 1 or -giants[0] > h: 
# NO 출력
    print('NO')
# 가장 큰 거인의 키 출력
    print(-giants[0])
# 아니면
else:
# 모든 거인의 키가 센티보다 작아지면 YES와
    print('YES')
# 마법 사용 횟수 출력
    print(count)

