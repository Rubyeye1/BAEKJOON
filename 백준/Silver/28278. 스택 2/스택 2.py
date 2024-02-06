import math
import sys
N = int(sys.stdin.readline())

stack = []                                    # 파이썬은 리스트가 곧 스택이다.
for i in range(N):
    command = sys.stdin.readline().split()    # 문제에서 문자와 숫자를 포함해서 입력을 N번만큼 받아야하는데 이 입력은 공백(띄어쓰기)로 구분을 해야 하므로
                                              # sys.stdin.readline().split()을 사용하면 띄어쓰기 단위로 리스트에 반환하기 때문에 편리하다.
    if command[0] == '1':
        stack.append(command[1])

    elif command[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == '3':
        print(len(stack))

    elif command[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            a = len(stack)
            print(stack[a-1])