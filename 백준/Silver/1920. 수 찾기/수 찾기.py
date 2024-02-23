import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())                                       # 숫자 N을 입력받는다.
L = list(map(int, sys.stdin.readline().split()))                    # 리스트 L을 입력받는다.
L.sort()                                                            # 이분탐색을 사용하기 위해서 L을 오름차순으로 sort해준다.

M = int(sys.stdin.readline())                                       # 숫자 M을 입력받는다.
Check = list(map(int, sys.stdin.readline().split()))                # 리스트 Check를 입력받는다.

def binary(temp):                                                   # 이분탐색 함수인 binary를 구현한다.

    start = 0                                                       # 이분탐색의 기본으로 start는 0으로 정하고.
    end = N-1                                                       # end는 N-1로 정한다.

    while start <= end:                                             # 그리고 start가 end보다 작거나 같을 때까지 반복해준다.(이 조건을 어긴다는 것은 존재하지 않는다는 것)
        mid = int((start + end) / 2)                                # mid는 start와 end를 더하고 2를 나눈후에 소수점 첫째자리에서 내림해주도록 한다(int를 사용하면 소수점이 제거된다).
        if L[mid] == temp:                                          # 만약 mid에서 찾고자하는 값을 찾았다면.
            print(1)                                                # 1을 출력하고 return으로 함수를 종료해준다.
            return
        elif L[mid] <= temp:                                        # mid에서 찾고자하는 값을 못 찾았고 이 값이 mid보다 큰 값이라면.
            start = mid + 1                                         # start를 mid+1로 설정하여 범위를 반으로 줄여준다.
        else:                                                       # mid에서 찾고자하는 값을 못 찾았고 이 값이 mid보다 작은 값이라면.
            end = mid - 1                                           # end를 mid-1로 설정하여 범위를 반으로 줄여준다.

    print(0)                                                        # 위 반복문을 빠져나왓다는 것은 리스트 L에 찾고자하는 값이 없다는 뜻이므로 0을 출력해주고 return으로 함수를 종료한다.
    return

for i in range(M):                                                  # 리스트 Check안의 원소들을 반복문 for문을 통해서 하나씩 검사해준다!!
    binary(Check[i])