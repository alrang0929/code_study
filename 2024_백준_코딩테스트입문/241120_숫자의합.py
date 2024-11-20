import sys
sys.stdin = open("input.txt","r")

# data = input().split
num = int(input())
data = list(map (int,input().split()))
answer = 0;

for i in data:
    answer += i

print(answer)