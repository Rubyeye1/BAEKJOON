import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):

    N = int(sys.stdin.readline())

    result = 0
    grade = 0

    for i in range(N):

        tempCredit, tempGrade = map(float, sys.stdin.readline().split())
        result += tempCredit
        grade += tempCredit * tempGrade

    GPA = grade / result

    print(int(result), round(GPA,1))