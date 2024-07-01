import math
import sys
from collections import deque
import copy
import datetime


M, N = map(int, sys.stdin.readline().split())
Dic = {'0':"zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"} # 영어 대응 딕셔너리 만들기.
L = []

for i in range(M, N+1):
    temp = ' '.join([Dic[j] for j in str(i)]) # 입력받은 i에 대해서 일의 자리 수, 십의 자리 수 한 글자 씩 나눠서 띄어쓰기로 join 함수를 사용하여 문자열을 생성.
    L.append([i, temp])                       # 이후 숫자와 그에 해당하는 영어를 리스트에 추가.

L.sort(key = lambda x : x[1])                 # 이후 영어들을 기준으로 사전순으로 정렬하기 위해서 x[1]을 기준으로 정렬한다.

for i in range(len(L)):
    if i % 10 == 0 and i != 0:                # 한 줄에 10개씩 출력.
        print()
    print(L[i][0], end=' ')