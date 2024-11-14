
def factorial(N):
    if N == 0 or N == 1: 
        return 1
    else:
        return N * factorial(N-1)

# 작성한 함수 다음에 입력 + 출력 할 것
N = int(input())
print(factorial(N))