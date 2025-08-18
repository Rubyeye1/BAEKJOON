import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

W, H = map(int, sys.stdin.readline().split())
print(round((W * H) * 0.5, 1))