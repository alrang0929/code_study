import sys
import heapq

input = sys.stdin.read
data = input().strip().split("\n")

# 입력 파싱
jewel_cnt, bag_cnt = map(int, data[0].split())
info_data = [tuple(map(int, line.split())) for line in data[1:jewel_cnt + 1]]
bag_inven = list(map(int, data[jewel_cnt + 1:]))

# 보석과 가방 정렬
info_data.sort(key=lambda x: x[0])  # 보석 무게 기준 정렬
bag_inven.sort()  # 가방 무게 오름차순 정렬

# 우선순위 큐(힙)와 결과 초기화
max_heap = []  # 가격을 최대 힙으로 관리
money = 0
jewel_index = 0

# 가방을 하나씩 처리
for current_bag in bag_inven:
    # 현재 가방에 담을 수 있는 보석 추가 (무게 조건 충족)
    while jewel_index < len(info_data) and info_data[jewel_index][0] <= current_bag:
        heapq.heappush(max_heap, -info_data[jewel_index][1])  # 가격을 음수로 추가
        jewel_index += 1

    # 가장 큰 가격의 보석을 담기
    if max_heap:
        money -= heapq.heappop(max_heap)  # 최대 가격 보석 담기 (음수니까 다시 -)

print(money)
