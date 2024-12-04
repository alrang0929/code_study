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
