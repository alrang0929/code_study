# https://www.acmicpc.net/problem/2805

def wood_cutter(n, m, trees):
    low, high = 0, max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # 잘린 나무의 길이 계산
        total = sum(max(0, tree - mid) for tree in trees)

        if total >= m:  # 필요한 나무 길이 이상인 경우
            result = mid  # 현재 높이를 기록
            low = mid + 1  # 더 높은 높이를 탐색
        else:
            high = mid - 1  # 높이를 낮춰 더 많은 나무를 얻음

    return result

# 입력 처리
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 결과 출력
print(wood_cutter(n, m, trees))
