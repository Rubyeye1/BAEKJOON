import sys                       # sys.stdin.readline()을 사용하기 위한 sys import.
from collections import deque    # 파이썬에서 큐를 사용하기 위한 deque import

N = int(sys.stdin.readline())    # 정수 N을 입력받고.
queue = deque([])                # queue를 선언.

for i in range(1, N + 1):        # 먼저 1부터 정수 N까지를 queue에 넣어야하므로.
    queue.append(i)              # queue.append를 써서 queue에 넣는다.
for i in range(N-1):             # 이후 마지막으로 카드 한 장을 남기기 위하여 N-1번 동작을 반복한다.
    queue.popleft()              # 제일 위에 있는 카드를 버리고.
    a = queue.popleft()          # 이후 그 다음 카드를 버리고(pop).
    queue.append(a)              # 가장 밑으로 옮긴다(append).

print(queue[0])                  # 이러면 마지막에 딱 한 장이 남게 되고 그것을 출력한다.