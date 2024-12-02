'''
https://www.acmicpc.net/problem/1946

T = 테스트 케이스
M = 지원자의 숫자
서류심사 성적 면접성적

예외X

'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for _ in range(T):
    input()
    a, b = list(map(int, input().split()))
    print(a, b)
    