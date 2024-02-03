import sys
from collections import deque                                           # BFS를 구현하기 위해서 deque를 사용해준다.

N, M = map(int, sys.stdin.readline().split())                           # N, M을 입력 받아준다.
maze = [list(map(int, input())) for _ in range(N)]                      # 2차원 배열을 입력 받아준다.
q = deque()                                                             # 큐를 선언해주고.
q.append((0, 0))                                                        # q에 초기값인 (0, 0) 좌표를 넣어준다.
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]                                  # 이후 붙어있는 한 칸씩 움직여서 탐색할 것이므로 위쪽 아래쪽 오른쪽 왼쪽 이렇게 4개의 기본 좌표를 만들어 둔다. 

def bfs():                                                              # bfs함수를 만든다.
    while q:                                                            # 큐에 원소가 하나도 없을 때까지(제일 끝 점에 도착할 때까지) 반복한다.
        x, y = q.popleft()                                              # 먼저 큐에서 한 원소를 pop 해주고.
        for i in range(4):                                              # 4가지 기본 좌표에 대해서 검사해준다.
            tempx = x + d[i][0]
            tempy = y + d[i][1]
            if 0 <= tempx < N and 0 <= tempy < M:                       # 만약 기본 좌표를 더한 좌표가 미로판 안에 있고.
                if maze[tempx][tempy] == 1:                             # 그 값이 1이어서 움직일 수 있는 좌표이면.
                    maze[tempx][tempy] = maze[x][y] + 1                 # 이동을 할 것이므로 움직일 수 있는 좌표의 값에 움직인 거리를 누적해서 더해준다.
                    q.append((tempx, tempy))                            # 그리고 큐에 좌표를 추가해준다.

bfs()                                                                   # 함수 실행.
print(maze[N-1][M-1])                                                   # 끝점에 도달할 경우의 최단거리를 출력해준다.