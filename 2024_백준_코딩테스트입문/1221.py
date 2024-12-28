# https://www.acmicpc.net/problem/27961

import sys
import math
input = sys.stdin.readline

# 입력
n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    # log2
    res = math.ceil(round(math.log(n, 2), 10))
    print(res+1)