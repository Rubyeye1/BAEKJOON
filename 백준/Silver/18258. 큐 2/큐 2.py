import sys                                              # sys.stdin.realine()을 사용하기 위한 sys import.
from collections import deque                           # 파이썬에서 큐를 사용하기 위한 deque 라이브러리!

n = int(sys.stdin.readline())                           # sys.stdin.readline()을 이용하여 정수 n을 입력받고.

queue = deque([])                                       # queue를 deque를 이용하여 만든다.

for i in range(n):                                      # n번 반복.
    command = sys.stdin.readline().split()              # 명령을 sys.stdin.readline().split()을 이용하여 입력받는다. 띄어쓰기를 기준으로 배열에 입력된다.
    if command[0] == 'push':                            # 만약 명령어가 push라면 그 다음에 있는 것을 queue에 append 한다.
        queue.append(command[1])
    elif command[0] == 'pop':                           # 만약 명령어가 pop이라면 queue에 하나도 없을 때에는 -1을 출력하고 그게 아니라면 큐의 가장 앞에 있는 정수를 빼고 출력한다.
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':                          # 만약 명령어가 size라면 queue에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif command[0] == 'empty':                         # 만약 명령어가 empty라면 큐에 아무것도 안 들어있으면 1, 무언가라도 들어있으면 0을 출력한다.
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':                         # 만약 명령어가 front라면 큐에 아무것도 안 들어있으면 -1, 들어있으면 가장 앞의 정수를 출력한다.
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':                          # 만약 명령어가 back이라면 큐에 아무것도 안 들어있으면 -1, 들어있으면 제일 뒤의 정수를 출력한다.
        if not queue:
            print(-1)
        else:
            print(queue[-1])