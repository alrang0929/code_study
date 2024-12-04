'''
https://www.acmicpc.net/problem/1524

첫째줄 테스트 케이스 = T (T <=100)
세준이 병사 = N
세비의 병사 = M

[조건]
1. 살아있는 병사중 제일 약한 병사가 죽는다
2. 제일 약한 병사가 양 팀에 있다면? 세비의 제일 약한 병사가 죽음
3. 최후의 1명이 남을 때 가지 반복
4. 승리자 출력
        세준 이김 : S
        세비 이김 : B
        병사 엾음 : C


[예제 입력1]

2 <== 테스트 케이스

1 1 <== 병사 수 N M 
1 <== M
1 <== N

3 2
1 3 2
5 5



'''

# t = int(input())
# for i in range(t) :
#     input()	# 빈줄 읽기
#     N, M = map(int, input().split())
#     sj = sorted(list(map(int, input().split())), reverse=True)
#     sb = sorted(list(map(int, input().split())), reverse=True)
    
#     while sj and sb :	# 세준, 세비 병사 리시트가 비어있으면 while문 종료
#         if sj[-1] >= sb[-1] :	# 같거나 크면 세비의 병사 죽음
#             sb.pop()
#         else :
#             sj.pop()
    
#     if sj :
#         print('S')
#     elif sb :
#         print('B')
#     else :
#         print('C')
        
        
import heapq

t = int(input())
for _ in range(t): #O(n)
    input()  # 테스트 케이스 사이의 빈 줄 처리

    # 병사 수 입력
    N, M = map(int, input().split())

    # 병사 리스트를 Min-Heap으로 변환
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    heapq.heapify(sj)  # 세준의 병사들 O(n)
    heapq.heapify(sb)  # 세비의 병사들 O(n)

    # 전투 시작
    while sj and sb:
        if sj[0] >= sb[0]:  # 세준 병사가 세비 병사보다 약하거나 같으면
            heapq.heappop(sb)  # 세비의 병사 제거 O(log n)
        else:
            heapq.heappop(sj)  # 세준의 병사 제거 O(log n)

    # 결과 출력
    if sj:  # 세준의 병사가 남아있으면 세준 승리
        print('S')
    elif sb:  # 세비의 병사가 남아있으면 세비 승리
        print('B')
    else:  # 둘 다 병사가 남아있지 않으면 무승부
        print('C')

# 전체 시간복잡도: O(n log n)