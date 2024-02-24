import math
import sys
from collections import deque
import copy

K, N = map(int, sys.stdin.readline().split())                           # N, K를 입력받는다.
L = []                                                                  # 리스트 L을 만들어놓는다.

for i in range(K):                                                      # K개의 랜선의 길이를 입력받아서 리스트에 넣어준다.
    temp = int(sys.stdin.readline())
    L.append(temp)

result = 0                                                              # 최종 결과를 저장할 result 변수.
start = 1                                                               # 이분탐색을 하기 위해 필요한 start 변수.
end = max(L)                                                            # 이분탐색을 하기 위해 필요한 end 변수.

while start <= end:                                                     # 이분탐색을 한다. 이분탐색을 고려하는 이유는 이 문제를 풀기 위해서 1부터 리스트의 가장 큰 수까지 전부 고려해서 하나씩 L을 나누어보면.
                                                                        # 당연히 답을 얻을 수 있지만 이는 시간이 너무 많이 걸리므로 이분탐색을 이용한다.
    mid = (start + end) // 2                                            # mid는 start+end를 2로 나눈 정수 몫.

    tempResult = 0                                                      # 그리고 mid로 랜선들을 나눈 개수를 저장하기 위해서 tempResult 변수를 선언해준다.

    for i in range(K):                                                  # tempResult에 현재의 mid값으로 랜선들을 자른 개수를 tempResult 변수에 저장해준다.
        tempResult = tempResult + (L[i] // mid)

    if tempResult >= N:                                                 # 만약 tempResult가 N보다 크거나 같은 상황이라면 일단 필요한 랜선의 개수는 만족하는데.
        start = mid + 1                                                 # 잘게 쪼갰다는 뜻이므로 더 큰 숫자로 쪼개주기 위해서 start를 mid+1로 옮겨준다.
        if result < mid:                                                # 필요한 랜선의 개수는 만족하는 상황에서 문제에서 요구하는 최대 랜선의 길이를 구해야 하므로.
            result = mid                                                # result 변수와 현재 조건을 만족하는 mid값을 계속 비교해서 갱신함으로써 최대 길이를 구해준다.
    else:                                                               # tempResult가 N보다 작은 상황이면 너무 큰 숫자로 쪼갰다는 뜻이므로 end를 mid-1로 지정해준다.
        end = mid - 1

print(result)                                                           # 최종결과 출력!