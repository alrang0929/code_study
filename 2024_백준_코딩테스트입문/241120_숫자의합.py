import sys
sys.stdin = open("input.txt","r")

# data = input().split
num = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum=sum + int(i)

print(sum)