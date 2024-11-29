'''

[예제 입력]
4 4
11 TwinkleStar C C G G A A G
8 Marigold E D E F E E D
23 DoYouWannaBuildASnowMan C C C G C E D
12 Cprogramming C C C C C C C
E D E
C G G
C C C
C C G

[예제 출력]
Marigold
!
?
TwinkleStar
'''

import sys
# 1. 입력처리

data = sys.stdin.read().splitlines()
# 2. 변수 선언
    # 2-1. N = 노래 수
N = int(data[0])
print(N)
    # 2-2. 노래 문제 수

# 3. 요소들 가져오기 
    # 3-1 민준의 뇌속
    # T = 노래제목 길이
    # S = 노래제목 문자열 
    # a = 음계, 공백구분

    # 3-2 주어진 문제 3음계 

# 출력: 동일한 노래1 = 노래 제목 / 두개이상 = ? / 없음 = !