# https://www.acmicpc.net/problem/1181
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''
# 1. 들어온 단어들의 길이 순으로 정리
# 2. 길이가 같으면 사전 순으로<<
# key = 단어, value = 글수

# 1. 글자수로 정렬

import sys
input = sys.stdin.read
data = input().strip().split("\n")
voca = list(set(map(str,data[1:])))
voca_dict = {value: len(value) for value in voca}
'''
{'but': 3, 'cannot': 6, 'wait': 4, 'it': 2, 'yours': 5, 'hesitate': 8, 'i': 1, 'more': 4, 'no': 2, 'im': 2, 'wont': 4}
'''
# 1. 들어온 단어들의 길이 순으로 정리
sorted_voca = dict(sorted(voca_dict.items(), key = lambda x: (len(x[0]), x[0])))

# 2. 길이가 같으면 사전순으로 정렬
same_len = []
index = 0

# sorted_voca를 순회하면서 처리
for key, value in sorted_voca.items():
    if not same_len:  # 처음 시작 시 첫 번째 단어 처리
        same_len.append(key)  # 첫 번째 단어 추가
    elif len(key) == len(same_len[0]):  # 길이가 같으면 same_len에 추가
        same_len.append(key)
    else:
        # 길이가 다르면, same_len을 정렬하고 sorted_voca에 추가
        same_len.sort()  # 사전순으로 정렬
        for word in same_len:
            sorted_voca[word] = len(word)  # 정렬된 단어들을 sorted_voca에 추가
        same_len = [key]  # 새로운 길이의 단어는 새로운 same_len 리스트에 넣기

# 마지막에 남은 same_len 리스트도 정렬하고 sorted_voca에 반영
if same_len:
    same_len.sort()
    for word in same_len:
        sorted_voca[word] = len(word)

# 최종 출력
for key, value in sorted_voca.items():
    print(key)
    




# for key, value in sorted_voca.items():
#     same_len = {}
#     next_voca = sorted_voca[index]
#     if len(common_voca) == len(next_voca):
#         same_len.append(common_voca, next_voca)
#         sorted_voca[sorted(same_len)]
#         index += 1
#         next_voca = sorted_voca[index]
#         same_len = {}
#     else: break

    
# for문을 도는데 만약 앞의 값과 value가 같냐?
# 그럼 same_len 배열에 추가하고 순서를 바꾼 후 다시 맨 뒤에 추가해라






