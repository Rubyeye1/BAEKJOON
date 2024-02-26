import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())                               # N을 입력받는다.
L = list(map(int, sys.stdin.readline().split()))            # 리스트 L을 입력받는다.

L.sort()                                                    # L을 오름차순으로 정리한다.

                                                            # 예를 들어보니 규칙을 찾을 수 있었다.
                                                            # 123 일때에는 최소값이 7이고, 124 일때에는 최소값이 8이고, 125 일때에는 최소값이 4, 126 일때에는 최소값이 4, 127 일때에는 최소값이 4.
                                                            # 만약 현재의 인덱스까지의 원소값을 전부 다 더한 누적값 + 1 보다 다음 인덱스의 원소값이 크면 지금까지의 누적합 + 1 이 만들 수 없는 무게 중 최소값이 된다. 
                                                            
result = 0                                                  # 최종 결과를 담을 변수 result.
temp = 0

for weight in L:                                            # 리스트의 원소에 대해서.
    if temp + 1 < weight:                                   # 만약 현재 인덱스의 원소값이 바로 전까지의 리스트 원소들의 누적합 + 1 보다 크다면.
        break                                               # 중지한다.
    temp = temp + weight                                    # 크지 않다면 현재 인덱스의 원소값도 더한다.

print(temp+1)                                               # 반복문 도중 중지해서 빠져나왔을때에는 리스트 원소들의 누적합 + 1을 출력해야하고.
                                                            # 끝까지 반복문을 잘 마친 경우에도 어차피 리스트 전체 원소들의 누적합 + 1을 출력해야하기 때문에 +1을 더해서 최종 결과를 출력해준다.