import math
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())                               # N, M을 입력받는다.
L = [list(map(int, input())) for _ in range(N)]                             # L을 입력받는다.
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]                                      # 상하좌우 한 칸씩 이동할 수 있으므로 좌표셋을 만들어둔다.
q = deque()                                                                 # bfs를 구현하기 위해서 deque를 만든다.
q.append([0, 0, 0])                                                         # 큐에 처음 좌표인 0, 0, 0을 넣어둔다.
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]                       # L 크기의 3차원 배열을 생성하는데 여기서 3번째 인덱스는 벽을 부쉈는지 안 부쉈는지를 체크하는 용도이고 visit 자체의 값은 L과 비교하여서.
                                                                            # 이 좌표를 방문하였는가, 방문하지 않았는가를 체크하는 용도이다. 방문했으면 1로 변경해주고 이게 누적되면 최단거리가 된다.
visit[0][0][0] = 1                                                          # visit의 첫 좌표는 L의 0, 0에서 시작하기 때문에 자동으로 방문하므로 1로 두고 시작한다.
def bfs():                                                                  # bfs를 구현한다.
    while q:                                                                # q가 텅 빌 때까지 밑을 반복한다.
        x, y, z = q.popleft()                                               # 큐에서 좌표를 pop해서 x, y, z에 넣어준다.
        for k in range(4):                                                  # 좌표셋을 하나씩 더해가면서 체크를 해주는데.
            dx = x + d[k][0]
            dy = y + d[k][1]

            if 0 <= dx < N and 0 <= dy < M:                                 # 맵 상에 좌표가 있을경우.
                if L[dx][dy] == 0 and visit[dx][dy][z] == 0:                # 만약 좌표셋을 더한 이 좌표의 L의 값이 0(벽이 없어서 움직일 수 있다)이고 visit[dx][dy][z]가 0이면(아직 방문하지 않았다).
                    q.append([dx, dy, z])                                   # 큐에 좌표를 넣어주고.
                    visit[dx][dy][z] = visit[x][y][z] + 1                   # visit에 이 좌표를 방문했다고 체크해주고 거리를 누적해준다.
                elif L[dx][dy] == 1 and z == 0:                             # 만약 좌표셋을 더한 이 좌표의 L의 값이 1(벽이 있어서 움직일 수 없다)이고 z가 0(아직 벽을 안부숴서 한 번 부술 수 있는 기회가 남아있다)이면.
                    visit[dx][dy][z+1] = visit[x][y][z] + 1                 # visit[dx][dy][z+1] 이렇게 z에 1을 더해서 이 좌표를 벽을 부숴서 올 수 있었다고 체크해주고 거기에 거리를 누적해준다.
                    q.append([dx, dy, z+1])                                 # 그리고 큐에 z+1(벽을 부술 기회를 사용하였다)을 해준 좌표를 추가해준다.

        if x == N-1 and y == M-1:                                           # 만약 위 과정을 반복하여 끝까지 왔으면.
            return visit[x][y][z]                                           # 최단거리를 return 해준다.

    return -1                                                               # 만약 끝까지 못오고 벽에 막혔으면 -1을 return 해준다.

print(bfs())                                                                # bfs함수를 실행하고 최종 return 값을 출력한다!