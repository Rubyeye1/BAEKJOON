import math
import sys
from collections import deque
import copy

N, S = map(int, sys.stdin.readline().split())                   # N, S 를 입력받는다.
L = list(map(int, sys.stdin.readline().split()))                # 원소를 리스트화해서 저장해놓는다.

result = 0                                                      # 최종 결과인 reuslt 변수.

def dfs(idx, sum):                                              # 깊이 우선 탐색인 DFS를 구현한다.
    global result                                               # result 변수를 사용해야하므로 global변수로 지정해놓는다.

    if (idx == N):                                              # 만약 현재 인덱스(idx)와 N이 같다면 범위를 벗어나므로 return한다.
        return
    sum = sum + L[idx]                                          # sum에 리스트의 현재 값을 더한다.

    if sum == S:                                                # 만약 이 경우의 sum이 구하려는 S와 같다면 경우의 수(result)를 하나 플러스해준다.
        result = result + 1

    dfs(idx + 1, sum)                                           # 그리고 인덱스를 하나 더하여 재귀로 함수를 실행해주는데 이 때 현재 인덱스의 리스트의 원소 값을 포함하는 경우와.
    dfs(idx + 1, sum - L[idx])                                  # 현재 인덱스의 리스트의 원소 값을 포함하지 않는 경우 이렇게 둘로 나누어서 재귀를 각각 실행해서 경우의 수를.
                                                                # 깊이 우선 탐색으로 전부 돌아서 구해준다.
    
dfs(0, 0)                                              # dfs(0, 0)으로 시작해준다.

print(result)                                                   # 최종 결과 출력!