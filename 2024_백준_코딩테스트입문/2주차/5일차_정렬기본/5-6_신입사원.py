'''
https://www.acmicpc.net/problem/1946

T = 테스트 케이스
M = 지원자의 숫자
서류심사 성적 면접성적

예외X

그리디 법칙:

전체를 비교할 수 있는데
1명 1명씩 비교해서 나은 값들을 선택한게
최종적으로 최고의 신입사원을 뽑는다 

'''
import sys
input = sys.stdin.read

data = input().strip().split("\n")
T = int(data[0])  # 테스트 케이스 수
results = []
index = 1

for _ in range(T):
    N = int(data[index])  # 지원자 수
    index += 1

    # 서류 심사와 면접 점수를 각각 리스트로 저장
    doc_ranks = []
    interview_ranks = []

    for i in range(N):
        doc, interview = map(int, data[index + i].split())
        doc_ranks.append(doc)
        interview_ranks.append(interview)

    index += N

    # zip을 이용해 서류와 면접 순위를 묶고, 서류 기준으로 정렬
    combined = zip(doc_ranks, interview_ranks)
    sorted_combined = sorted(combined)  # 서류 성적 기준으로 정렬

    # 선발 과정
    selected = 0
    min_interview_rank = float('inf')  # 면접 성적 최소값

    for _, interview_rank in sorted_combined:
        if interview_rank < min_interview_rank:  # 면접 성적이 최소값보다 낮으면 선발
            selected += 1
            min_interview_rank = interview_rank

    results.append(selected)

# 결과 출력
print("\n".join(map(str, results)))
