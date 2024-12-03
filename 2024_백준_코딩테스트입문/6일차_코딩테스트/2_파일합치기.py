'''
https://www.acmicpc.net/problem/13975



소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다. 
소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다. 
이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐나가고, 
최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 
최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, 

1.C1, C2, C3, C4가 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 

이 파일들을 합치는 과정에서, 
먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 


이때 비용 60이 필요하다. 
그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 
최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 
다른 방법으로 파일을 합치면 비용을 줄일 수 있다. 

먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 
최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이때 필요한 총 비용은 70+80+150=300 이다.


이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.

입력
첫줄: 프로그램의 입력은 T개의 테스트 데이터, 

[테스트 데이터]
1행: 소설을 구성하는 장의 수
2행: 파일의 크기

파일의 크기는 10,000을 초과하지 않는다.


2

4
40 30 30 50

15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32



'''

import sys, heapq

# 최소힙으로 정렬하여 맨 앞의 값과 맨 뒤의 값을 더함
load = sys.stdin.read
data = load().strip().split("\n")
T = int(data[0])
index = 1
results = []

# 최소 힙 생성
for _ in range(T):
    file_sizes = list(map(int, data[index + 1].split()))  # 파일 크기 리스트
    index += 2 #다음 타입을 위한 인덱스 갱신
    
    # 최소 힙 생성
    heapq.heapify(file_sizes)
    total_cost = 0
    
# 가장 작은 파일과 다음으로 작은 파일 더하기
    while len(file_sizes) > 1:
        file1 = heapq.heappop(file_sizes)  # 가장 작은 파일
        file2 = heapq.heappop(file_sizes)  # 두 번째로 작은 파일
        merge_cost = file1 + file2
        total_cost += merge_cost
        
        heapq.heappush(file_sizes, merge_cost)  # 합친 파일 다시 힙에 삽입
    results.append(total_cost)
    
for result in results:
    print(result)


    

    