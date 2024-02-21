import math
import sys
from collections import deque
import copy

N, K = map(int, sys.stdin.readline().split())               # N, K를 입력받는다.
DP = [[0]*1001 for _ in range(1001)]                        # 동적 프로그래밍(DP)을 구현하기 위해서 N의 범위가 1000까지 이므로 1000까지 2차원 배열을 만들어 놓는다.

for i in range(1, N+1):                                     # 조합의 앞 범위는 1부터 N까지, 나누는 것의 범위는 0부터 i까지 지정해주고.
    for j in range(0, i+1):

        if i == j:                                          # 만약 i와 j가 같다면 i개중에 i개를 뽑는 것이므로 경우의 수가 하나이므로 1로 지정해주고.
            DP[i][j] = 1

        elif j == 0:                                        # j가 0이라면 하나도 안 뽑는 경우라서 1로 지정해주고.
            DP[i][j] = 1

        else:                                               # 위의 경우가 아니라면 조합의 점화식에 의해서 더해준다.
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j])

print(DP[N][K] % 10007)                                     # 최종 결과 출력!