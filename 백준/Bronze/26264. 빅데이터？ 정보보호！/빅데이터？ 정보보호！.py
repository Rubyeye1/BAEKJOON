import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
memo = input()

bd = memo.count('bigdata')
sc = memo.count('security')

if bd > sc:
    print('bigdata?')
elif bd < sc:
    print('security!')
else:
    print('bigdata? security!')