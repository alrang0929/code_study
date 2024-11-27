
    for command in commands:
    if command.startswith("push_back"):
        _, num = command.split()
        decue.append(int(num))  # 맨 뒤에 추가

    elif command.startswith("push_front"):
        _, num = command.split()
        decue.appendleft(int(num))  # 맨 앞에 추가

    elif command == "front":  # front 명령
        if decue:  # 덱이 비어 있지 않으면
            print(decue[0])  # 맨 앞의 값 출력
        else:
            print(-1)  # 비어 있으면 -1 출력

    elif command == "back":  # back 명령
        if decue:  # 덱이 비어 있지 않으면
            print(decue[-1])  # 맨 뒤의 값 출력
        else:
            print(-1)  # 비어 있으면 -1 출력

    elif command == "size":  # size 명령
        print(len(decue))  # 덱의 길이 출력

    elif command == "empty":  # empty 명령
        print(1 if not decue else 0)  # 비어 있으면 1, 아니면 0 출력

    elif command == "pop_front":  # pop_front 명령
        if decue:  # 덱이 비어 있지 않으면
            print(decue.popleft())  # 맨 앞의 값 제거하고 출력
        else:
            print(-1)  # 비어 있으면 -1 출력

    elif command == "pop_back":  # pop_back 명령
        if decue:  # 덱이 비어 있지 않으면
            print(decue.pop())  # 맨 뒤의 값 제거하고 출력
        else:
            print(-1)  # 비어 있으면 -1 출력
            
            