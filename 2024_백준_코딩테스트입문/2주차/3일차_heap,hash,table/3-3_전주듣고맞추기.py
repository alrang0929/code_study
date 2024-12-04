
# import sys

# # 1. 입력처리
# sys.stdin = open("input.txt","r")
# data = input().splitlines()
# '''
# ['4 4', 
# '11 TwinkleStar C C G G A A G', 
# '8 Marigold E D E F E E D', 
# '23 DoYouWannaBuildASnowMan C C C G C E D', 
# '12 Cprogramming C C C C C C C', 
# 'E D E', 
# 'C G G', 
# 'C C C', 
# 'C C G']

# '''
# # 2. 변수 선언
# # 2-1.노래 수 num[0]=민준 뇌 속 노래 수 / num[1]=노래 문제 수
# num = list(map(int,data[0].split()))
# sing = int(num[1])
# # 음계: C, D, E, F, G, A, B 

# # 결과저장
# results = []

# # 3. 요소들 가져오기
# # 3-2 민준의 뇌속에서 뽑아오기
# minjun = list(map(str,data[1:num[0]+1]))


# '''
# ['11 TwinkleStar C C G G A A G',
# '8 Marigold E D E F E E D',
# '23 DoYouWannaBuildASnowMan C C C G C E D',
# '12 Cprogramming C C C C C C C']
# '''
# quiz = list(map(str,data[num[0]+1:]))

# for quiz_item in quiz:
#     quiz_split = quiz_item.split()  # 퀴즈의 첫 세 음 분리
#     matched_titles = []  # 일치하는 노래 제목 저장

#     for item in minjun:
#         minjun_brain = item.split()  # 민준 데이터의 각 줄 분리
#         minjun_title = minjun_brain[1]  # 노래 제목
#         minjun_a = minjun_brain[2:]  # 음계 데이터

#         # 퀴즈의 첫 세 음과 민준 음계의 첫 세 음 비교
#         if quiz_split == minjun_a[:3]:
#             matched_titles.append(minjun_title)

#     # 출력 조건 처리
#     if len(matched_titles) == 1:
#         results.append(matched_titles[0])  # 유일한 제목 출력
#     elif len(matched_titles) > 1:
#         results.append("?")  # 여러 곡이 일치
#     else:
#         results.append("!")  # 일치하는 곡 없음

# # 결과 출력
# for result in results:
#     print(result)

import sys
from collections import defaultdict

# 입력 처리
# input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄: N (노래 수), M (퀴즈 수)
N, M = map(int, data[0].split())

# 노래 데이터 저장
song_dict = defaultdict(list)  # 키: 첫 세 음, 값: 노래 제목 리스트
print(song_dict)
for i in range(1, N + 1):
    line = data[i].split()
    title = line[1]  # 노래 제목
    first_three_notes = tuple(line[2:5])  # 첫 세 음 추출
    song_dict[first_three_notes].append(title)

# 퀴즈 처리
results = []
for i in range(N + 1, N + M + 1):
    quiz_notes = tuple(data[i].split())  # 퀴즈 음계
    if quiz_notes in song_dict:
        if len(song_dict[quiz_notes]) == 1:
            results.append(song_dict[quiz_notes][0])  # 유일한 제목
        else:
            results.append("?")  # 여러 곡
    else:
        results.append("!")  # 없음

# 결과 출력
sys.stdout.write("\n".join(results) + "\n")
