from collections import deque

testCases = int(input())

for _ in range(testCases):
    n, m = map(int, input().split())

    queue = deque()
    priorities = [0] * 9

    documents = list(map(int, input().strip().split()))
    for i in range(n):
        priority = documents[i]
        queue.append((i, priority))
        priorities[priority - 1] += 1

    printOrder = 0

    while queue:
        current = queue.popleft()
        hasHigherPriority = False

        for i in range(current[1], 9):
            if priorities[i] > 0:
                hasHigherPriority = True
                break

        if hasHigherPriority:
            queue.append(current)
        else:
            printOrder += 1
            priorities[current[1] - 1] -= 1
            if current[0] == m:
                print(printOrder)
                break