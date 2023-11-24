import sys                                    # 한 두줄 정도를 입력받는 경우에는 input()을 사용해도 괜찮지만 여러 줄을 계속해서 입력받아야 할 때에는
N = int(sys.stdin.readline())                 # 시간초과가 발생할 수 있기 때문에 sys.stdin.readline()을 사용해야한다.
                                              # 이를 사용하기 위한 sys import.
stack = []                                    # 파이썬은 리스트가 곧 스택이다. 스택 선언
for i in range(N):
    command = sys.stdin.readline().split()    # 문제에서 문자와 숫자를 포함해서 입력을 N번만큼 받아야하는데 이 입력은 공백(띄어쓰기)로 구분을 해야 하므로
                                              # sys.stdin.readline().split()을 사용하면 띄어쓰기 단위로 리스트에 반환하기 때문에 편리하다.
    if command[0] == 'push':                  # 예를들어 push 2 명령어를 입력 받았을 때 command에는 [push, 2] 이런식으로 리스트안에 명령어가 들어가있는 형태가 되고
        stack.append(command[1])              # push는 정수를 스택에 넣는(쌓는) 연산이기 때문에 command[1]을 stack에 추가한다.

    elif command[0] == 'pop':                 # pop일때는 가장 위에 있는 정수를 빼고 그 수를 출력, 만약 스택에 들어있는 정수가 없는 경우에 -1을 출력해야하기 때문에
        if len(stack) == 0:                   # len으로 스택의 길이를 검사해서 만약 정수가 없으면 -1을 반환하고
            print(-1)
        else:                                 # 아니면 pop으로 가장 위의 정수를 빼서 print로 출력한다.
            print(stack.pop())                # 파이썬의 리스트.pop 라이브러리 함수는 가장 오른쪽의 원소를 삭제하고 반환하는 것!

    elif command[0] == 'size':                # size일때에는 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))

    elif command[0] == 'empty':               # empty일때에는 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':                 # top일 때에는 가장 위의 정수를 출력하는데 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stack) == 0:
            print(-1)
        else:
            a = len(stack)
            print(stack[a-1])