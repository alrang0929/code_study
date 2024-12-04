'''
문제풀이
1. 받아온 문자열을 쪼갠다
2. 두 수를 비교한다
3. 작은 수를 리버스 시켜 출력
'''
# arrrr = "734 893"
arr = input().split()
if arr[0][::-1] > arr[1][::-1] :
    print(arr[1][::-1])
else : print(arr[0][::-1])