'''
https://www.acmicpc.net/problem/17207

가장 일이 바쁘지 않은 사람에게 일처리를 맡기기
=  최종 일량이 가장 작은 사람을 찾는 문제

ex)

일 = 5

 인서=1
 준석=2
 정우=3 
 진우=4
 영기=5
 
 A, B graph = NxN
 A[x][y] = x번 사람이 예상한 y번째 일의 난이도
 B[x][y] = x번 사람이 예상한 y번째 일의 처리 시간
 
A[x][y]*B[x][y] = x번 사람의 y번째 일의 예상 일량

'''

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    A = [list(map(int, data[i].split())) for i in range(5)]
    B = [list(map(int, data[i + 5].split())) for i in range(5)]
    
    names = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
    priorities = {"Youngki": 0, "Jinwoo": 1, "Jungwoo": 2, "Junsuk": 3, "Inseo": 4}
    final_workloads = []
    
    for x in range(5):
        total_workload = 0
        for y in range(5):
            expected_workload = sum(A[x][i] * B[i][y] for i in range(5))
            total_workload += expected_workload
        final_workloads.append((total_workload, names[x]))
    
    # 가장 일이 바쁘지 않은 사람 찾기
    final_workloads.sort(key=lambda x: (x[0], priorities[x[1]]))
    print(final_workloads[0][1])

if __name__ == "__main__":
    main()
