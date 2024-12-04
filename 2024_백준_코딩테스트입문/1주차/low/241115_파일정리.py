'''
[조건]
1. 파일을 지우지 말것

2-1. 각 확장자가 몇 개씩 있는지 [확장자명 갯수] 포맷으로 출력
2-2. 결과물을 내림차 sort

'''

# 파이썬 여러줄 문자열 선언 """ """
data = input()
def run_code(input_str):
   # splitlines: 줄단위 문자열을 리스트로 반환하는 함수
   # split('\n) 과 동일

   # 확장자별 개수를 저장
   ext_cnt = {}
   # 1. 받은 문자열을 줄단위로 분해
   line_str = input_str.splitlines()
   
   # 2. for문을 돌며 파일명과 확장자명 분할
   for item in line_str:
      split_item = item.split(".")
      #2-1 2번째 인덱스 즉, 확장자명만 뽑음
      #2-2 만약 split_item의 배열이 1개 이상이냐?
      if len(split_item) > 1:
         # 2-3그러면 extention에 두번째 값을 넣어라 
         ext = split_item[1]
         ext_cnt[ext] = ext_cnt.get(ext, 0) + 1
         # [확장자 비교 시작]
   result = sorted(ext_cnt.items(), key=lambda x: (x[1], -x[0]))
   return [f"{k} {v}" for k, v in result]
               
# extention 누적
result = run_code(data)
print(result)
