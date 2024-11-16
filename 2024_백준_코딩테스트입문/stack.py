
# 정상적인 괄회: VPS = YES, 아님? NO

def find_vps(s):
    stack = [] 
    for c in s:
        if c =='(':
            stack.append(c)
        elif c == ')':
            # 처음부터 열린괄호다? 정상X
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
                
n = int(input()) #테스트 케이스의 수
results = []

for i in range(n):
    target = input()
    results.append("YES" if find_vps(target) else "NO")

for result in results:
    print(result) 
