import math
import sys
from collections import deque
import copy                                                                 # 2차원 배열 깊은 복사를 하기 위한 copy.

N, M = map(int, sys.stdin.readline().split())                               # N, M을 입력받는다.
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]        # L을 입력받는다.
d = [(0,1), (1,0), (0,-1), (-1,0)]                                          # 기본 좌표셋을 만들어준다.
q = deque()                                                                 # bfs에 사용할 큐를 만들어준다.
result = 0                                                                  # 최종 결과인 result 변수를 만들어준다.

def wallMaking(count):                                                      # 일단 벽 3개를 무조건 세워야하므로 L의 모든 0에 대해서 완전 탐색을 생각해볼 수 있는데 이를 백트래킹 함수로 구현해본다.

    if count == 3:                                                          # 만약 count가 3이면 지금 벽 3개를 전부 세웠다는 뜻이므로 이 상태에서 bfs()를 실행해주고 return 한다.
        bfs()
        return

    for i in range(N):                                                      # 좌표의 값이 0인 모든 경우에 대해서 3개의 벽을 세우는 재귀함수를 만든다.
        for j in range(M):
            if L[i][j] == 0:                                                # 만약 좌표의 값이 0이면.
                L[i][j] = 1                                                 # 그 좌표에 벽을 세우고.
                wallMaking(count+1)                                         # 벽을 세운 횟수를 하나 더해서 카운팅 해주고 재귀함수를 호출한다.
                L[i][j] = 0                                                 # 위 함수가 끝났다는 것은 return 했다는 의미이므로 아까 세운 벽을 허물어준다.

def bfs():                                                                  # bfs를 구현한다.

    global result                                                           # 최종 결과를 담을 글로벌 변수 result.
    LSecond = copy.deepcopy(L)                                              # L을 깊은 복사한 LSecond 배열을 만들어준다. 기존 L은 wallMaking함수에서 계속 벽을 세우는 작업을 하고 있으므로.
                                                                            # 현재 벽을 3개 세우고 실행된 bfs에서의 L만 고려하기 위해서 깊은복사를 해서 만들어준다.

    for e in range(N):                                                      # 좌표의 값이 2(바이러스)라면 전염시킬 수 있으므로 큐에 초기 좌표들을 추가해준다.
        for r in range(M):
            if LSecond[e][r] == 2:
                q.append((e, r))

    while q:                                                                # 큐에 바이러스 좌표들이 다 없어질 때까지 반복한다.
        x, y = q.popleft()                                                  # 좌표 하나를 큐에서 뽑아서.

        for i in range(4):                                                  # 상하좌우로 검사해준다.
            dx = x + d[i][0]
            dy = y + d[i][1]

            if 0 <= dx < N and 0 <= dy < M:
                if LSecond[dx][dy] == 0:                                    # 만약 좌표의 값이 0이라면.
                    LSecond[dx][dy] = 2                                     # 전염시켜주고 큐에 추가해준다.
                    q.append((dx, dy))

    zeroCnt = 0                                                             # 최종 결과를 구하기 위한 zeroCnt 변수.
    for a in range(N):
        for b in range(M):
            if LSecond[a][b] == 0:                                          # 안전지대인 0을 세서 zeroCnt에 넣어준다.
                zeroCnt = zeroCnt + 1                                       # 만약 바이러스에 전부 감염이 되었다면 자동으로 안전지대의 개수는 0일 것이기 때문에 result와 계속 비교해주면 최댓값을 구할 수 있다.

    result = max(result, zeroCnt)                                           # result 변수와 zeroCnt를 비교해서 최댓값을 만든다.

wallMaking(0)                                                               # 백트래킹 함수 실행.
print(result)                                                               # 최종 결과 출력!