import math
import sys
from collections import deque
import copy

N, M, V = map(int, sys.stdin.readline().split())                            # N, M, V 입력받기.
Link = [[0] * (N+1) for _ in range(N+1)]                                    # 간선을 저장해주기 위한 2차원 배열 Link.

for i in range(M):                                                          # 정점과 정점이 연결된 곳들을 저장해준다.
    a, b = map(int, sys.stdin.readline().split())
    Link[a][b] = 1
    Link[b][a] = 1

Q = deque()                                                                 # bfs에서 사용할 큐.
def dfs(vertex):                                                            # dfs를 구현한다.
    print(vertex, end=" ")                                                  # 먼저 함수에 들어온 정점을 출력해주고(띄어쓰기 한 번씩 해서 출력해준다).
    visit[vertex] = 1                                                       # 그 정점을 방문했다고 visit 배열에 표시해준다.
    for i in range(1, N+1):                                                 # 그리고 정점들의 관계를 for문으로 하나씩 봐서.
        if Link[vertex][i] == 1 and visit[i] == 0:                          # 이후 만약 지금 정점에서 연결된 부분이 있으며 거기가 방문한 곳이 아님을 검사한 후에.
            dfs(i)                                                          # 재귀함수를 사용하면 다음 정점과 연결된 부분을 계속 깊숙히 탐색하므로 dfs(i)를 써준다.

def bfs(vertex):                                                            # bfs를 구현한다.
    Q.append(vertex)                                                        # 먼저 시작 정점인 vertex를 큐에 추가해준다.
    visit[vertex] = 1                                                       # 이후 시작 정점을 방문했다고 visit 배열에 표시해준 후에.
    while Q:
        temp = Q.popleft()                                                  # 반복문으로 큐에서 정점들을 하나씩 pop해서 큐가 아예 빌 때까지 계속해서 반복한다.
        print(temp, end=" ")                                                # pop된 정점을 일단 출력하고.
        for i in range(1, N+1):                                             # 이후 정점들의 관계를 for문으로 하나씩 봐서
            if Link[temp][i] == 1 and visit[i] == 0:                        # 만약 지금 정점에서 연결된 부분이 있으며 아직 방문하지 않았으면.
                Q.append(i)                                                 # 큐에 정점들을 추가해주고(시작 정점에서 가장 가까운 부분들을 먼저 다 추가하고 출력할 것이고 이후에도 같은 방식이므로 너비 우선 탐색이 된다.)
                visit[i] = 1                                                # 이후 정점들을 방문했다고 visit 배열에 저장해준다.


visit = [0] * (N+1)                                                         # 방문했는지 여부를 저장할 visit 배열.
dfs(V)
print()
visit = [0] * (N+1)                                                         # dfs함수에서 visit 배열의 값이 달라 졌을 것이므로 한 번 더 초기화한다.
bfs(V)