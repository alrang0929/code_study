'''
https://www.acmicpc.net/problem/2018

문제요약:
자연서 N을 나타낼 수 있는 더하기 식을 구하시오

문제 핵심: 정수 N에 대해 연속된 자연수의 합으로 N을 표현할 수 있는 경우 찾기

답: 경우의 개수

투 포인터:
두개의 index룰 사용하여 점진적으로 조정하여 문제를 해결

pointer start, end 사용

start = 1
end = 1
sum = 초기값 1, start + end

 N = 15
 
 포인트 이동 조건
 sum < n : end 1 앞으로 이동
 sum > n : start 1 앞으로 이동, count 1 증가가
 sum = n : 알고리즘 종료

'''
N = int(input())
start = 1
end = 1
sum = 1
count = 0

while start <= N :
    if sum == N:
        count += 1
        sum -= start
        start += 1
    elif sum < N:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1
print(count)
        