import math
import sys
from collections import deque
import copy

def binary(start, end, find, List):                                     # 이분탐색 함수로 현재 찾아야 하는 값(find)가 처음으로 위치한 인덱스를 반환시켜준다.
    while(start < end):
        m = (start+end)//2
        if(List[m] < find):
            start = m+1
        else:
            end = m
    return end


N, H = map(int, sys.stdin.readline().split())                           # N, H를 입력받는다.
Seock = []                                                              # 석순의 장애물의 크기를 보관하는 리스트 Seock.
Jong = []                                                               # 종유석의 장애물의 크기를 보관하는 리스트 Jong.

for i in range(N):                                                      # 석순에는 입력의 짝수번째, 종유석에는 입력의 홀수번째로 각각 리스트에 장애물의 크기를 삽입해준다.
    temp = int(sys.stdin.readline())
    if i % 2 == 0:
        Seock.append(temp)
    else:
        Jong.append(temp)

Seock.sort()                                                            # 석순과 종유석을 sort로 오름차순으로 정렬해준다.
Jong.sort()

minResult = 500000                                                      # 파괴해야하는 장애물의 최솟값을 저장하기 위한 변수 minResult.
Results = [0] * 500001                                                  # 인덱스마다 장애물을 파괴한 횟수를 저장하기 위한 Results.
minCount = 0                                                            # 장애물을 파괴한 횟수의 최소값에 해당하는 구간을 세기 위한 minCount.

for i in range(1, H+1):                                                 # 1번부터 H번까지 구간마다 몇 번 장애물을 파괴하는지 세주고 이 횟수를 Results에 저장해주는 작업.

    tempResult = 0                                                      # 구간마다 장애물을 파괴시키는 횟수를 저장하기 위한 tempResult

    SeockIdx = binary(0, len(Seock), i, Seock)                     # 이중 for문을 사용해서 인덱스를 검사하면 시간초과가 발생하므로 이분탐색을 사용해준다.
    JongIdx = binary(0, len(Jong), H-i+1, Jong)

    tempResult = N - SeockIdx - JongIdx                                 # tempResult에 2분의N에서 SeockIdx를 뺀 값, 2분의N에서 JongIdx를 뺀 값을 저장해준다.(최종적으로 장애물을 전부 깬 횟수가 담긴다)

    Results[i] = tempResult                                             # 그리고 최종적으로 이 i구간에서 장애물(석순, 종유석)을 파괴한 개수를 Results에 저장해준다.
    minResult = min(minResult, Results[i])                              # 이후 현재 구간에서 장애물을 파괴한 횟수와 minResult를 비교하면서 장애물을 파괴한 개수의 최소값을 계속 갱신시켜서 최소값을 구해준다.

for i in range(1, H+1):
    if Results[i] == minResult:                                         # 만약 minResult(장애물을 파괴한 최소값)이 현재 구간의 장애물 파괴횟수와 같은 경우에는.
        minCount = minCount + 1                                         # 장애물 파괴의 최소값 구간이라는 뜻이므로 minCount를 하나씩 증가시켜준다.

print(minResult, minCount)                                              # 최종결과 출력!