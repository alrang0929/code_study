'''
https://www.acmicpc.net/problem/16112


메이플스토리 뉴비 키파가 드디어 레벨 200을 달성하고 5차 전직이라는 시스템을 이용해 캐릭터를 더욱 강력하게 만들려고 합니다. 
5차 전직을 하려면 먼저 퀘스트를 통해 아케인스톤이라는 아이템을 받아야 합니다. 
아케인스톤을 활성화시키면 캐릭터가 얻는 경험치를 아케인스톤에 모을 수 있습니다. 

5차 전직을 하기 위해서는 총 n개의 퀘스트를 진행해서 

n개의 아케인스톤을 받아야 하며, 
각각의 아케인스톤에 5억 이상의 경험치를 모으면 5차 전직을 진행할 수 있는 자격이 주어집니다.

i번째 퀘스트를 진행하면 ai의 경험치와 i번째 아케인스톤이 주어집니다. 
퀘스트로 얻는 경험치도 사냥으로 얻는 것과 똑같은 경험치이기 때문에, 
i번째 퀘스트의 보상 경험치를 받을 때 활성화되어 있던 아케인스톤에는 ai의 경험치가 추가됩니다.



원래 메이플스토리에서는 한 번에 하나의 아케인스톤만 활성화시켜 놓을 수 있고, 
각각의 아케인스톤에는 최대 5억의 경험치를 채울 수 있습니다. 
그러나 해킹에는 자신이 있었던 메린이 키파는 


1. 아케인스톤의 최대 경험치 제한 X, 
2. 최대 k개의 아케인스톤이 동시에 활성화 가능

 예를 들어 
 1번째와 3번째 아케인스톤이 활성화되어 있는 상태에서 
 2번째 퀘스트를 진행해 100,000의 경험치와 2번째 아케인스톤을 획득하면, 
 1번째와 3번째 아케인스톤에 각각 100,000의 경험치가 추가되고 
 2번째 아케인스톤은 모인 경험치가 0인 상태로 받게 됩니다.

키파는 퀘스트를 원하는 순서대로 진행할 수 있지만, 같은 퀘스트를 두 번 이상 진행할 수는 없습니다. 
키파는 퀘스트를 진행하면서 아케인스톤을 적절히 활성화 또는 비활성화시켜서 아케인스톤에 모인 경험치의 합을 최대화하고 싶습니다. 
모인 경험치의 합이 커지면 어쨌든 기분이 좋으니까요. 키파를 대신해서 이 값을 구해 주세요!



[입력]
첫째 줄에 정수 n과 k(1 ≤ k ≤ n ≤ 3 · 105)가 주어집니다.

둘째 줄에 n개의 정수가 공백을 사이에 두고 주어집니다. i번째 정수는 ai이며 0보다 크고 108보다 작거나 같습니다.

3<=전체 아케인 스톤 2 <=활성화된 아케인 스톤
100 300 200

800



먼저 첫 번째 퀘스트를 진행하고 첫 번째 아케인스톤을 받은 뒤 활성화시킵니다. 
그 다음 세 번째 퀘스트를 진행하고 세 번째 아케인스톤을 받은 뒤 활성화시킵니다. 
마지막으로 두 번째 퀘스트를 진행합니다.

이 경우 첫 번째 아케인스톤에 500, 세 번째 아케인스톤에 300의 경험치가 모여 합이 800이 되고, 이보다 모인 경험치의 합을 크게 할 수는 없습니다.


'''
# import heapq
# 최대 아케인에 최소 아케인을 더 한 합
# 300+200
# 200+100
# = 800

#활성화된 아케인 수 만큼 루프를 돌면서
# 최대힙 + 최소힙
# 사용한 최소힙 최대힙 삭제
# 다음 최대힙+ 다음 최소힙

# 입력 처리
# n, k = map(int, input().split())
# exp = list(map(int, input().split()))
# max_heap = [-x for x in exp] 
# heapq.heapify(max_heap)
# max_exp = 0
# index = 1
# total = 0
# for _ in range(k):    
#     current_max_exp = -heapq.heappop(max_heap)
#     if len(max_heap) >= 2:
#         next_exp = -heapq.heappop(max_heap)
#         total += (current_max_exp + next_exp)
#         heapq.heappop(max_heap)
#         index +=1
#         current_max_exp = next_exp
#     else:
#         break
    
    
# print(total)

import heapq

n, k = map(int, input().split())
exp = list(map(int, input().split()))
max_heap = [-x for x in exp] 
heapq.heapify(max_heap)

total = 0

for _ in range(k):    
    if len(max_heap) >= 2:  # 힙에 값이 최소 2개 이상 있는지 확인
        current_max_exp = -heapq.heappop(max_heap)  
        next_exp = -heapq.heappop(max_heap)         
        total += (current_max_exp + next_exp)      
        heapq.heappush(max_heap, -next_exp)         
    else:
        break  # 힙에 값이 부족하면 종료

print(total)
