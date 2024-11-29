# 국회의원 선거
'''
다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다.

다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다. >> 값 변동X

현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.

다솜이는 기호 1번이다. 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.

>>다솜이 기호 1번, 최다 득표자 = 국회의원

예를 들어서, 마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 다솜이는 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면, 국회의원에 당선이 된다.

돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.
>>미쳤어 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
>>매수 당한사람 = 100% 다솜이표

다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.

N 국회의원:  50이하
M 동네사람: 100 이하



[입력]
첫째 줄에 후보의 수 N이 주어진다. 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다. N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.

[예제 입력]
3

기호1=5
기호2=7
기호3=7

기호2번 기호3번의 표를 하나쌕 뺏으면 됨! 따라서

[예제 출력]
2

'''
import heapq
import sys

# 1. 입력받기
data = sys.stdin.read().splitlines()
n = int(data[0])  # 후보의 수
dasom = int(data[1])  # 다솜의 표
votes = list(map(int, data[2:]))  # 다른 후보들의 표
count = 0  # 매수 횟수

# 1-2. votes를 최대 힙으로 관리하기 위한 음수로 저장
max_heap = [-v for v in votes]  # 최대 힙을 위해 음수로 변환
heapq.heapify(max_heap)  # 리스트를 힙 구조로 변환

# 2. 예외 처리: 후보가 다솜 혼자인 경우
if n == 1:
    print(0)  # 매수 필요 없음
else:
    # 2-1. 다솜의 표가 최대가 될 때까지 반복
    while max_heap and -max_heap[0] >= dasom:
        # 가장 많은 표를 가진 후보를 매수
        max_votes = -heapq.heappop(max_heap)
        dasom += 1
        count += 1
        max_votes -= 1

        # 매수 후 표가 남아 있으면 다시 힙에 삽입
        if max_votes > 0:
            heapq.heappush(max_heap, -max_votes)

    print(count)









# # 1. 입력받기
# data = sys.stdin.read().splitlines()
# # 1-1. 다솜이가 들고있는 표
# dasom = int(data[0])
# # 1-2. 출마자들의 표
# votes = list(map(int, data[1:]))
# # 1-3. 매수 횟수
# bribes = 0

# # 2. 예외 처리: 다솜이가 이미 최다 득표자인 경우
# if not votes or dasom > max(votes):  # 다른 후보가 없거나 다솜이가 최다 득표자인 경우
#     print(0)  # 매수 필요 없음
#     exit()

# # 2. 다른 후보들의 득표수를 최대 힙으로 관리
# # heap은 최소힙이 기본값, 따라서 음수로 전환하여 출마자 중 최대값을 찾는다
# max_heap = [-v for v in votes]  # 최대 힙을 위해 음수로 변환
# heapq.heapify(max_heap)

# # 3. 최다 득표자가 될 때까지 매수 작업을 계속한다!
# # 예외 방지를 위한 max_heap and
# while max_heap and dasom <= -max_heap[0]:
#     # 가장 많은 표를 가진 후보의 표를 줄이고, 다솜의 표를 늘림
#     max_votes = -heapq.heappop(max_heap)  # 가장 많은 표를 가진 후보의 표
#     max_votes -= 1  # 해당 후보의 표를 1 줄임
#     dasom += 1  # 다솜의 표를 1 증가
#     bribes += 1  # 매수 횟수 증가

#     # 줄어든 표가 0보다 크면 다시 힙에 넣기
#     if max_votes > 0:
#         heapq.heappush(max_heap, -max_votes)

# print(bribes)


# # 2. 다른 출마자들과 표 비교
# for i in range(1,len(votes)):
#     # print(votes[i])
#     # 2-1. case1: 다솜이보다 표가 많을 경우
#     if votes[1] <= votes[i]:
#         votes[i] -= 1
#         dasom_votes+=1
#         # 2-2. case2: 다솜이와 표가 같을 경우 
#     elif votes[1] == votes[i]: 
#         dasom_votes=1
#     # 2-1. case3: 다솜이만 있을 경우  
#     else:
#         dasom_votes=0

# print(dasom_votes)