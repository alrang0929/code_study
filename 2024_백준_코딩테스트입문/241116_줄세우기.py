import sys
sys.stdin = open("input.txt","r")
#  우선순위가 높을 수록 앞으로, 
# 참고 강의: https://www.youtube.com/watch?v=Wz2F7HbPD4s

N = int(input())
# 1. lst: 학생 위치 배열
# 인자들을 int로 변환하여 list로 쪼갬
lst = list(map(int, input().split())) #[0, 1, 1, 3, 2] : 학생들 번호표
alst = [n for n in range(1, N+1)] #lst와 위치값 일치, 학생 자리
# for 앞의 n = 리스트 표현식(list comprehension)**에서 출력될 값, n에 담긴 숫자를 리스트로 그대로 출력하겠다

for i in range(N):# i번째 학생의 위치를 순서대로 이동처리
    n, t = lst[i], alst[i] #앞으로 이동할 칸 수, 위치 일치시키기
    for j in range(i,i-n,-1):
        alst[j] = alst[j-1] # 현재 학생 번호에 이전 학생 번호 덮어쓰기
    alst[i-n] = t
print(*alst)