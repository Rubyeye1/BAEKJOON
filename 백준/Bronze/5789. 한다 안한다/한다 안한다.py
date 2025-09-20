import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
	temp = list(input())
	
	i = len(temp) // 2 - 1
	
	if temp[i] == temp[-i-1]:
		print('Do-it')
	else:
		print('Do-it-Not')