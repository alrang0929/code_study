# https://www.acmicpc.net/problem/18870

# 좌표압축
# 1. data 원본
# 2. 원본 중복값 제거 set
# 3. 제거 후 sort
# 4. sort한 값에 인덱스 저장
# 5. 원본 데이터를 key 값으로 하여 values 가져옴, 그것을 배열에 추가 후 출력




import sys

input = sys.stdin.read
data = input().strip().split("\n")

origin = list(map(int,data[1].split()))
sorted_origin = sorted(set(origin))
mapping_origin = {value: index for index, value in enumerate(sorted_origin)}
# enumerate(): 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴

answer = [mapping_origin[x] for x in origin]

print(" ".join(map(str, answer)))