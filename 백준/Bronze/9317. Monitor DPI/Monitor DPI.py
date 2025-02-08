import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    D, HOR, VER = map(float, input().split())
    if D == 0 and HOR == 0 and VER == 0:
        break

    W = 16 * D / 337 ** 0.5
    H = (9 / 16) * W

    print('Horizontal DPI: %.2f' % (HOR/W))
    print('Vertical DPI: %.2f' % (VER/H))